from __future__ import annotations

import sqlite3
from datetime import datetime, timezone

from .paths import DB_PATH, ensure_dirs


def connect() -> sqlite3.Connection:
    ensure_dirs()
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    con.execute(
        """
        CREATE TABLE IF NOT EXISTS activity (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            created_at TEXT NOT NULL,
            app_slug TEXT NOT NULL,
            action TEXT NOT NULL,
            detail TEXT
        )
        """
    )
    con.commit()
    return con


def log_activity(app_slug: str, action: str, detail: str = "") -> None:
    with connect() as con:
        con.execute(
            "INSERT INTO activity(created_at, app_slug, action, detail) VALUES (?, ?, ?, ?)",
            (
                datetime.now(timezone.utc).isoformat(timespec="seconds"),
                app_slug,
                action,
                detail,
            ),
        )
        con.commit()


def recent_activity(limit: int = 20) -> list[sqlite3.Row]:
    with connect() as con:
        return con.execute(
            """
            SELECT created_at, app_slug, action, detail
            FROM activity
            ORDER BY id DESC
            LIMIT ?
            """,
            (limit,),
        ).fetchall()
