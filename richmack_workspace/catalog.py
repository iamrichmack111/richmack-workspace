from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class WorkspaceApp:
    name: str
    package: str
    emoji: str
    description: str
    slug: str


APPS: tuple[WorkspaceApp, ...] = (
    WorkspaceApp(
        name="Wize Wizard",
        package="wize-wizard",
        emoji="🪄",
        description="Strategy, PERT, communications, tasks, and journal planner.",
        slug="wize-wizard",
    ),
    WorkspaceApp(
        name="Language Ninja",
        package="language-ninja",
        emoji="🧠",
        description="NLP sentiment training, analysis, notes, and export workstation.",
        slug="language-ninja",
    ),
    WorkspaceApp(
        name="Pot of Mannah",
        package="pot-of-mannah",
        emoji="🍯",
        description="Terminal nutrition and training intelligence.",
        slug="pot-of-mannah",
    ),
    WorkspaceApp(
        name="ExerxEye",
        package="ExerxEye",
        emoji="⚙️",
        description="Exercise intelligence, workout tracking, and progress analytics.",
        slug="exerxeye",
    ),
    WorkspaceApp(
        name="Hebrew Fuzzy Study",
        package="hebrew-fuzzy-study",
        emoji="📜",
        description="Hebrew lexical search, Tanakh reader, scholar reference, and annotation.",
        slug="hebrew-fuzzy-study",
    ),
    WorkspaceApp(
        name="JinnLab",
        package="jinnlab",
        emoji="♟️",
        description="Game theory laboratory for Axelrod matches, Moran processes, and tournaments.",
        slug="jinnlab",
    ),
)


def by_slug(slug: str) -> WorkspaceApp:
    for app in APPS:
        if app.slug == slug:
            return app
    raise KeyError(slug)
