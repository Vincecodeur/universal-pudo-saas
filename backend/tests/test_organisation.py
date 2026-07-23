from universal_pudo_saas.organisations.models import Organisation


def test_organisation_creation() -> None:
    organisation = Organisation(
        name="Acme",
    )

    assert organisation.name == "Acme"


def test_organisation_inherits_base_entity_fields() -> None:
    organisation = Organisation(
        name="Acme",
    )

    assert hasattr(organisation, "id")
    assert hasattr(organisation, "created_at")
    assert hasattr(organisation, "updated_at")
    assert hasattr(organisation, "deleted_at")


def test_organisation_name_is_stored() -> None:
    organisation = Organisation(
        name="Acme Logistics",
    )

    assert organisation.name == "Acme Logistics"


def test_organisation_deleted_at_default_is_none() -> None:
    organisation = Organisation(
        name="Acme",
    )

    assert organisation.deleted_at is None