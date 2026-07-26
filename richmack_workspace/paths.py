from __future__ import annotations

from pathlib import Path

from platformdirs import user_data_dir

DATA_DIR = Path(user_data_dir("richmack-workspace", "Richmack"))
APPS_DIR = DATA_DIR / "apps"
DB_PATH = DATA_DIR / "workspace.db"
LOG_DIR = DATA_DIR / "logs"


def ensure_dirs() -> None:
    APPS_DIR.mkdir(parents=True, exist_ok=True)
    LOG_DIR.mkdir(parents=True, exist_ok=True)
