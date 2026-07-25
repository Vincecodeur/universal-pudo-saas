from universal_pudo_saas.database.session import (
    SessionLocal,
)
from universal_pudo_saas.memberships.models import (
    Membership,
)
from universal_pudo_saas.organisations.models import (
    Organisation,
)
from universal_pudo_saas.users.models import (
    User,
)


def test_membership_can_be_persisted() -> None:
    session = SessionLocal()

    try:
        organisation = Organisation(
            name="Membership Test Org",
        )

        user = User(
            email="membership@example.com",
            first_name="John",
            last_name="Doe",
            password_hash="hash",
        )

        session.add(organisation)
        session.add(user)

        session.commit()

        session.refresh(organisation)
        session.refresh(user)

        membership = Membership(
            organisation_id=organisation.id,
            user_id=user.id,
            role="admin",
        )

        session.add(membership)
        session.commit()
        session.refresh(membership)

        assert membership.id is not None
        assert membership.role == "admin"

    finally:
        session.delete(membership)
        session.delete(user)
        session.delete(organisation)
        session.commit()
        session.close()


def test_membership_can_be_retrieved() -> None:
    session = SessionLocal()

    try:
        organisation = Organisation(
            name="Retrieval Org",
        )

        user = User(
            email="retrieve@example.com",
            first_name="Jane",
            last_name="Doe",
            password_hash="hash",
        )

        session.add_all([organisation, user])
        session.commit()

        session.refresh(organisation)
        session.refresh(user)

        membership = Membership(
            organisation_id=organisation.id,
            user_id=user.id,
            role="viewer",
        )

        session.add(membership)
        session.commit()
        session.refresh(membership)

        retrieved = session.get(
            Membership,
            membership.id,
        )

        assert retrieved is not None
        assert retrieved.role == "viewer"

    finally:
        session.delete(membership)
        session.delete(user)
        session.delete(organisation)
        session.commit()
        session.close()


def test_membership_can_be_deleted() -> None:
    session = SessionLocal()

    try:
        organisation = Organisation(
            name="Delete Org",
        )

        user = User(
            email="delete-membership@example.com",
            first_name="Delete",
            last_name="User",
            password_hash="hash",
        )

        session.add_all([organisation, user])
        session.commit()

        session.refresh(organisation)
        session.refresh(user)

        membership = Membership(
            organisation_id=organisation.id,
            user_id=user.id,
            role="member",
        )

        session.add(membership)
        session.commit()
        session.refresh(membership)

        membership_id = membership.id

        session.delete(membership)
        session.commit()

        retrieved = session.get(
            Membership,
            membership_id,
        )

        assert retrieved is None

    finally:
        session.delete(user)
        session.delete(organisation)
        session.commit()
        session.close()
        