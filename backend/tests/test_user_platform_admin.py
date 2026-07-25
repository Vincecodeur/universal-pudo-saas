from universal_pudo_saas.users.models import User


def test_user_platform_admin_can_be_set_to_false() -> None:
    user = User(
        email="john@example.com",
        first_name="John",
        last_name="Doe",
        password_hash="hash",
        is_platform_admin=False,
    )

    assert user.is_platform_admin is False


def test_user_can_be_platform_admin() -> None:
    user = User(
        email="john@example.com",
        first_name="John",
        last_name="Doe",
        password_hash="hash",
        is_platform_admin=True,
    )

    assert user.is_platform_admin is True