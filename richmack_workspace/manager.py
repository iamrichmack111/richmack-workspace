from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from .catalog import WorkspaceApp
from .db import log_activity
from .paths import APPS_DIR, LOG_DIR, ensure_dirs


@dataclass(slots=True)
class AppStatus:
    installed: bool
    version: str | None = None
    entrypoint: str | None = None
    venv_dir: Path | None = None


class WorkspaceManager:
    def __init__(self) -> None:
        ensure_dirs()

    def _run_logged(self, app: WorkspaceApp, command: list[str]) -> None:
        """Run package-management commands without corrupting the Textual screen."""
        log_path = LOG_DIR / f"{app.slug}.log"
        with log_path.open("a", encoding="utf-8") as log:
            log.write("\n$ " + " ".join(command) + "\n")
            log.flush()
            result = subprocess.run(
                command,
                stdout=log,
                stderr=subprocess.STDOUT,
                text=True,
                check=False,
            )
        if result.returncode != 0:
            raise RuntimeError(
                f"Command failed for {app.name}. See log: {log_path}"
            )

    def app_dir(self, app: WorkspaceApp) -> Path:
        return APPS_DIR / app.slug

    def venv_dir(self, app: WorkspaceApp) -> Path:
        return self.app_dir(app) / ".venv"

    def python_path(self, app: WorkspaceApp) -> Path:
        if os.name == "nt":
            return self.venv_dir(app) / "Scripts" / "python.exe"
        return self.venv_dir(app) / "bin" / "python"

    def bin_dir(self, app: WorkspaceApp) -> Path:
        if os.name == "nt":
            return self.venv_dir(app) / "Scripts"
        return self.venv_dir(app) / "bin"

    def _metadata(self, app: WorkspaceApp) -> tuple[str | None, str | None]:
        python = self.python_path(app)
        if not python.exists():
            return None, None

        code = r"""
import importlib.metadata as md, json
package = __import__("sys").argv[1]
try:
    dist = md.distribution(package)
except md.PackageNotFoundError:
    print(json.dumps({"version": None, "entrypoint": None}))
    raise SystemExit(0)

eps = [
    ep.name for ep in dist.entry_points
    if ep.group == "console_scripts"
]
print(json.dumps({
    "version": dist.version,
    "entrypoint": eps[0] if eps else None,
}))
"""
        result = subprocess.run(
            [str(python), "-c", code, app.package],
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        if result.returncode != 0:
            return None, None
        try:
            data = json.loads(result.stdout.strip() or "{}")
        except json.JSONDecodeError:
            return None, None
        return data.get("version"), data.get("entrypoint")

    def status(self, app: WorkspaceApp) -> AppStatus:
        python = self.python_path(app)
        if not python.exists():
            return AppStatus(False, venv_dir=self.venv_dir(app))

        version, entrypoint = self._metadata(app)
        return AppStatus(
            installed=bool(version),
            version=version,
            entrypoint=entrypoint,
            venv_dir=self.venv_dir(app),
        )

    def install(self, app: WorkspaceApp) -> None:
        app_dir = self.app_dir(app)
        venv = self.venv_dir(app)
        app_dir.mkdir(parents=True, exist_ok=True)

        if not self.python_path(app).exists():
            self._run_logged(app, [sys.executable, "-m", "venv", str(venv)])

        python = self.python_path(app)
        self._run_logged(
            app, [str(python), "-m", "pip", "install", "--upgrade", "pip"]
        )
        self._run_logged(
            app, [str(python), "-m", "pip", "install", "--upgrade", app.package]
        )

        status = self.status(app)
        log_activity(
            app.slug,
            "install",
            f"{app.package} {status.version or ''}".strip(),
        )

    def update(self, app: WorkspaceApp) -> None:
        if not self.status(app).installed:
            self.install(app)
            return

        python = self.python_path(app)
        self._run_logged(
            app, [str(python), "-m", "pip", "install", "--upgrade", app.package]
        )
        status = self.status(app)
        log_activity(
            app.slug,
            "update",
            f"{app.package} {status.version or ''}".strip(),
        )

    def uninstall(self, app: WorkspaceApp) -> None:
        target = self.app_dir(app)
        if target.exists():
            shutil.rmtree(target)
        log_activity(app.slug, "uninstall", app.package)

    def launch_command(self, app: WorkspaceApp) -> list[str]:
        status = self.status(app)
        if not status.installed:
            raise RuntimeError(f"{app.name} is not installed.")
        if not status.entrypoint:
            raise RuntimeError(
                f"{app.package} is installed but exposes no console_scripts entry point."
            )

        exe = self.bin_dir(app) / status.entrypoint
        if os.name == "nt":
            candidates = [exe, exe.with_suffix(".exe")]
            for candidate in candidates:
                if candidate.exists():
                    return [str(candidate)]
        elif exe.exists():
            return [str(exe)]

        # Fallback through Python's script lookup environment.
        return [status.entrypoint]

    def launch(self, app: WorkspaceApp) -> int:
        command = self.launch_command(app)
        env = os.environ.copy()
        env["PATH"] = str(self.bin_dir(app)) + os.pathsep + env.get("PATH", "")
        log_activity(app.slug, "launch", " ".join(command))
        return subprocess.run(command, env=env, check=False).returncode
