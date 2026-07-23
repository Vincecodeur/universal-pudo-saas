from universal_pudo_saas.users.models import User


def test_user_creation() -> None:
    user = User(
        email="vincent@example.com",
        first_name="Vincent",
        last_name="Gueret",
        password_hash="hashed-password",
        is_active=True,
        is_verified=False,
    )

    assert user.email == "vincent@example.com"


def test_user_name_fields_are_stored() -> None:
    user = User(
        email="vincent@example.com",
        first_name="Vincent",
        last_name="Gueret",
        password_hash="hashed-password",
        is_active=True,
        is_verified=False,
    )

    assert user.first_name == "Vincent"
    assert user.last_name == "Gueret"


def test_user_authentication_fields_are_stored() -> None:
    user = User(
        email="vincent@example.com",
        first_name="Vincent",
        last_name="Gueret",
        password_hash="hashed-password",
        is_active=True,
        is_verified=False,
    )

    assert user.password_hash == "hashed-password"
    assert user.is_active is True
    assert user.is_verified is False


def test_user_last_login_default_is_none() -> None:
    user = User(
        email="vincent@example.com",
        first_name="Vincent",
        last_name="Gueret",
        password_hash="hashed-password",
        is_active=True,
        is_verified=False,
    )

    assert user.last_login_at is None


def test_user_inherits_base_entity_fields() -> None:
    user = User(
        email="vincent@example.com",
        first_name="Vincent",
        last_name="Gueret",
        password_hash="hashed-password",
        is_active=True,
        is_verified=False,
    )

    assert hasattr(user, "id")
    assert hasattr(user, "created_at")
    assert hasattr(user, "updated_at")
    assert hasattr(user, "deleted_at")


def test_user_deleted_at_default_is_none() -> None:
    user = User(
        email="vincent@example.com",
        first_name="Vincent",
        last_name="Gueret",
        password_hash="hashed-password",
        is_active=True,
        is_verified=False,
    )

    assert user.deleted_at is None
