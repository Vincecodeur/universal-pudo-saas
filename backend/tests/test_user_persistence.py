from universal_pudo_saas.database.session import (
    SessionLocal,
)
from universal_pudo_saas.users.models import (
    User,
)


def test_user_can_be_persisted() -> None:
    session = SessionLocal()

    try:
        user = User(
            email="persistence@example.com",
            first_name="John",
            last_name="Doe",
            password_hash="hashed-password",
        )

        session.add(user)
        session.commit()
        session.refresh(user)

        assert user.id is not None
        assert user.email == "persistence@example.com"

    finally:
        session.delete(user)
        session.commit()
        session.close()


def test_user_can_be_retrieved() -> None:
    session = SessionLocal()

    try:
        user = User(
            email="retrieval@example.com",
            first_name="Jane",
            last_name="Doe",
            password_hash="hashed-password",
        )

        session.add(user)
        session.commit()
        session.refresh(user)

        retrieved = session.get(
            User,
            user.id,
        )

        assert retrieved is not None
        assert retrieved.email == "retrieval@example.com"
        assert retrieved.first_name == "Jane"
        assert retrieved.last_name == "Doe"

    finally:
        session.delete(user)
        session.commit()
        session.close()


def test_user_authentication_fields_are_persisted() -> None:
    session = SessionLocal()

    try:
        user = User(
            email="auth@example.com",
            first_name="Auth",
            last_name="User",
            password_hash="hash123",
            is_active=True,
            is_verified=False,
        )

        session.add(user)
        session.commit()
        session.refresh(user)

        retrieved = session.get(
            User,
            user.id,
        )

        assert retrieved is not None
        assert retrieved.password_hash == "hash123"
        assert retrieved.is_active is True
        assert retrieved.is_verified is False

    finally:
        session.delete(user)
        session.commit()
        session.close()


def test_user_can_be_deleted() -> None:
    session = SessionLocal()

    try:
        user = User(
            email="delete@example.com",
            first_name="Delete",
            last_name="User",
            password_hash="hashed-password",
        )

        session.add(user)
        session.commit()
        session.refresh(user)

        user_id = user.id

        session.delete(user)
        session.commit()

        retrieved = session.get(
            User,
            user_id,
        )

        assert retrieved is None

    finally:
        session.close()