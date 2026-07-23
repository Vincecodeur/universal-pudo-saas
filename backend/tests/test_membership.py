import uuid

from universal_pudo_saas.memberships.models import Membership


def test_membership_creation() -> None:
    membership = Membership(
        organisation_id=uuid.uuid4(),
        user_id=uuid.uuid4(),
        role="ADMIN",
    )

    assert membership.role == "ADMIN"


def test_membership_role_is_stored() -> None:
    membership = Membership(
        organisation_id=uuid.uuid4(),
        user_id=uuid.uuid4(),
        role="USER",
    )

    assert membership.role == "USER"


def test_membership_has_valid_organisation_reference() -> None:
    organisation_id = uuid.uuid4()

    membership = Membership(
        organisation_id=organisation_id,
        user_id=uuid.uuid4(),
        role="ADMIN",
    )

    assert membership.organisation_id == organisation_id


def test_membership_has_valid_user_reference() -> None:
    user_id = uuid.uuid4()

    membership = Membership(
        organisation_id=uuid.uuid4(),
        user_id=user_id,
        role="ADMIN",
    )

    assert membership.user_id == user_id


def test_membership_inherits_base_entity_fields() -> None:
    membership = Membership(
        organisation_id=uuid.uuid4(),
        user_id=uuid.uuid4(),
        role="ADMIN",
    )

    assert hasattr(membership, "id")
    assert hasattr(membership, "created_at")
    assert hasattr(membership, "updated_at")
    assert hasattr(membership, "deleted_at")


def test_membership_deleted_at_default_is_none() -> None:
    membership = Membership(
        organisation_id=uuid.uuid4(),
        user_id=uuid.uuid4(),
        role="ADMIN",
    )

    assert membership.deleted_at is None