
from __future__ import annotations

from textual import work
from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import ModalScreen
from textual.widgets import Button, Footer, Header, Label, ListItem, ListView, Static

from .catalog import APPS, WorkspaceApp
from .db import recent_activity
from .manager import WorkspaceManager


WORKSPACE_ART = r"""
 ____  ___ ____ _   _ __  __    _    ____ _  __
|  _ \\|_ _/ ___| | | |  \\/  |  / \\  / ___| |/ /
| |_) || | |   | |_| | |\\/| | / _ \\| |   | ' /
|  _ < | | |___|  _  | |  | |/ ___ \\ |___| . \\
|_| \\_\\___\\____|_| |_|_|  |_/_/   \\_\\____|_|\\_\\

                 W O R K S P A C E
"""


class ConfirmUninstall(ModalScreen[bool]):
    CSS = """
    ConfirmUninstall {
        align: center middle;
    }

    #confirm-box {
        width: 64;
        height: auto;
        border: round $warning;
        padding: 1 2;
        background: $surface;
    }

    #confirm-buttons {
        height: auto;
        align-horizontal: center;
        margin-top: 1;
    }
    """

    def __init__(self, app_name: str) -> None:
        super().__init__()
        self.app_name = app_name

    def compose(self) -> ComposeResult:
        with Vertical(id="confirm-box"):
            yield Label(f"Remove {self.app_name} from Richmack Workspace?")
            with Horizontal(id="confirm-buttons"):
                yield Button("Cancel", id="cancel")
                yield Button("Remove", id="remove", variant="error")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.dismiss(event.button.id == "remove")


class RichmackWorkspace(App):
    TITLE = "Richmack Workspace"
    SUB_TITLE = "Terminal Intelligence Environment"

    CSS = """
    Screen {
        layout: vertical;
    }

    #brand {
        height: 9;
        content-align: center middle;
        text-align: center;
        text-style: bold;
        border-bottom: heavy $primary;
        padding: 0 1;
    }

    #instructions {
        height: 3;
        content-align: center middle;
        text-align: center;
        padding: 0 1;
        border-bottom: solid $boost;
    }

    #main {
        height: 1fr;
    }

    #apps {
        width: 42%;
        min-width: 38;
        border: round $primary;
    }

    #detail {
        width: 58%;
        padding: 1 2;
        border: round $secondary;
    }

    #big-icon {
        height: 5;
        content-align: center middle;
        text-align: center;
        text-style: bold;
        border-bottom: solid $boost;
        margin-bottom: 1;
    }

    #app-title {
        text-style: bold;
        text-align: center;
        margin-bottom: 1;
    }

    #description {
        margin-bottom: 1;
    }

    #status {
        margin: 1 0;
    }

    #actions {
        height: auto;
        margin-top: 1;
    }

    #actions Button {
        margin-right: 1;
    }

    #activity {
        margin-top: 2;
        height: 1fr;
        border-top: solid $boost;
        padding-top: 1;
    }

    ListItem {
        height: 3;
        padding: 1 2;
    }

    ListItem.--highlight {
        text-style: bold;
    }
    """

    BINDINGS = [
        ("enter", "launch", "Launch"),
        ("g", "install", "Get"),
        ("u", "update", "Update"),
        ("x", "uninstall", "Remove"),
        ("r", "refresh", "Refresh"),
        ("q", "quit", "Quit"),
    ]

    def __init__(self) -> None:
        super().__init__()
        self.manager = WorkspaceManager()
        self.selected_index = 0

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        yield Static(WORKSPACE_ART, id="brand")
        yield Static(
            "UP/DOWN Select   ENTER Launch   G Install   U Update   "
            "X Remove   R Refresh   Q Quit",
            id="instructions",
        )
        with Horizontal(id="main"):
            yield ListView(
                *[
                    ListItem(
                        Label(f"  {app.emoji}   {app.name}"),
                        id=f"app-{i}",
                    )
                    for i, app in enumerate(APPS)
                ],
                id="apps",
            )
            with Vertical(id="detail"):
                yield Static("", id="big-icon")
                yield Static("", id="app-title")
                yield Static("", id="description")
                yield Static("", id="package")
                yield Static("", id="status")
                with Horizontal(id="actions"):
                    yield Button("Launch", id="launch", variant="primary")
                    yield Button("Get", id="install")
                    yield Button("Update", id="update")
                    yield Button("Remove", id="uninstall", variant="error")
                yield Static("", id="activity")
        yield Footer()

    def on_mount(self) -> None:
        apps = self.query_one("#apps", ListView)
        apps.index = 0
        self.refresh_detail()

    def selected_app(self) -> WorkspaceApp:
        return APPS[self.selected_index]

    def on_list_view_highlighted(self, event: ListView.Highlighted) -> None:
        if event.item is None:
            return
        item_id = event.item.id or ""
        if item_id.startswith("app-"):
            self.selected_index = int(item_id.split("-", 1)[1])
            self.refresh_detail()

    def refresh_detail(self) -> None:
        app = self.selected_app()
        status = self.manager.status(app)

        self.query_one("#big-icon", Static).update(
            f"[bold]\n        {app.emoji}   {app.emoji}   {app.emoji}\n[/bold]"
        )
        self.query_one("#app-title", Static).update(f"[bold]{app.name}[/bold]")
        self.query_one("#description", Static).update(app.description)
        self.query_one("#package", Static).update(f"PyPI package: {app.package}")

        if status.installed:
            entry = status.entrypoint or "No console entry point detected"
            status_text = (
                f"[bold green]Installed[/bold green]\n"
                f"Version: {status.version}\n"
                f"Command: {entry}"
            )
        else:
            status_text = (
                "[yellow]Not installed[/yellow]\n"
                "Press G or choose Get to install this application."
            )

        self.query_one("#status", Static).update(status_text)

        rows = recent_activity(8)
        if not rows:
            activity = "[bold]Recent Activity[/bold]\nNo activity yet."
        else:
            lines = ["[bold]Recent Activity[/bold]"]
            for row in rows:
                stamp = row["created_at"].replace("T", " ")[:16]
                lines.append(f"{stamp}  {row['app_slug']:<20} {row['action']}")
            activity = "\n".join(lines)
        self.query_one("#activity", Static).update(activity)

    def notify_error(self, error: Exception) -> None:
        self.notify(str(error), severity="error", timeout=8)

    @work(thread=True, exclusive=True)
    def install_selected(self) -> None:
        app = self.selected_app()
        try:
            self.call_from_thread(
                self.notify,
                f"Installing {app.name} in the background…",
                timeout=5,
            )
            self.manager.install(app)
            self.call_from_thread(
                self.notify,
                f"{app.name} installed successfully.",
                severity="information",
            )
        except Exception as exc:
            self.call_from_thread(self.notify_error, exc)
        finally:
            self.call_from_thread(self.refresh_detail)

    @work(thread=True, exclusive=True)
    def update_selected(self) -> None:
        app = self.selected_app()
        try:
            self.call_from_thread(
                self.notify,
                f"Updating {app.name} in the background…",
                timeout=5,
            )
            self.manager.update(app)
            self.call_from_thread(
                self.notify,
                f"{app.name} update complete.",
            )
        except Exception as exc:
            self.call_from_thread(self.notify_error, exc)
        finally:
            self.call_from_thread(self.refresh_detail)

    def action_install(self) -> None:
        self.install_selected()

    def action_update(self) -> None:
        self.update_selected()

    def action_refresh(self) -> None:
        self.refresh_detail()
        self.notify("Workspace refreshed.")

    def action_launch(self) -> None:
        app = self.selected_app()
        try:
            if not self.manager.status(app).installed:
                self.notify(
                    f"{app.name} is not installed. Press G to install.",
                    severity="warning",
                )
                return

            with self.suspend():
                self.manager.launch(app)

            self.refresh_detail()
        except Exception as exc:
            self.notify_error(exc)

    def action_uninstall(self) -> None:
        app = self.selected_app()

        def after_confirm(remove: bool | None) -> None:
            if not remove:
                return
            try:
                self.manager.uninstall(app)
                self.notify(f"{app.name} removed.")
                self.refresh_detail()
            except Exception as exc:
                self.notify_error(exc)

        self.push_screen(ConfirmUninstall(app.name), after_confirm)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "launch":
                self.action_launch()
            case "install":
                self.action_install()
            case "update":
                self.action_update()
            case "uninstall":
                self.action_uninstall()


def main() -> None:
    RichmackWorkspace().run()


if __name__ == "__main__":
    main()
