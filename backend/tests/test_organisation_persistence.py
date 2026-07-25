from universal_pudo_saas.database.session import (
    SessionLocal,
)
from universal_pudo_saas.organisations.models import (
    Organisation,
)


def test_organisation_can_be_persisted() -> None:
    session = SessionLocal()

    try:
        organisation = Organisation(
            name="Persistence Test Organisation",
        )

        session.add(organisation)
        session.commit()
        session.refresh(organisation)

        assert organisation.id is not None
        assert organisation.name == (
            "Persistence Test Organisation"
        )

    finally:
        session.delete(organisation)
        session.commit()
        session.close()


def test_organisation_can_be_retrieved() -> None:
    session = SessionLocal()

    try:
        organisation = Organisation(
            name="Retrieval Test Organisation",
        )

        session.add(organisation)
        session.commit()
        session.refresh(organisation)

        retrieved = session.get(
            Organisation,
            organisation.id,
        )

        assert retrieved is not None
        assert (
            retrieved.name
            == "Retrieval Test Organisation"
        )

    finally:
        session.delete(organisation)
        session.commit()
        session.close()


def test_organisation_can_be_deleted() -> None:
    session = SessionLocal()

    try:
        organisation = Organisation(
            name="Deletion Test Organisation",
        )

        session.add(organisation)
        session.commit()
        session.refresh(organisation)

        organisation_id = organisation.id

        session.delete(organisation)
        session.commit()

        retrieved = session.get(
            Organisation,
            organisation_id,
        )

        assert retrieved is None

    finally:
        session.close()