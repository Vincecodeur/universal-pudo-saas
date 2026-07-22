from universal_pudo_saas.core.settings import get_settings


def test_database_url_exists() -> None:
    settings = get_settings()

    assert settings.database_url != ""