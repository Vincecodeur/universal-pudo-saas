from universal_pudo_saas.organisations.models import Organisation


def test_organisation_creation() -> None:
    organisation = Organisation(
        name="Test Organisation",
    )

    assert organisation.name == "Test Organisation"
    assert organisation.deleted_at is None