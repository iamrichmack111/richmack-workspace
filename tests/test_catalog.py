from richmack_workspace.catalog import APPS


def test_catalog_has_unique_slugs() -> None:
    slugs = [app.slug for app in APPS]
    assert len(slugs) == len(set(slugs))


def test_catalog_has_packages() -> None:
    assert all(app.package for app in APPS)
