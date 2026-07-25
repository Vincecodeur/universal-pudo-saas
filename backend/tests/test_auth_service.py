from universal_pudo_saas.auth.service import (
    authenticate_user,
    create_user_token,
)
from universal_pudo_saas.security.passwords import (
    hash_password,
)
from universal_pudo_saas.security.tokens import (
    decode_access_token,
)


def test_authenticate_user_success() -> None:
    password_hash = hash_password("secret123")

    assert authenticate_user(
        "secret123",
        password_hash,
    )


def test_authenticate_user_failure() -> None:
    password_hash = hash_password("secret123")

    assert not authenticate_user(
        "wrong-password",
        password_hash,
    )


def test_create_user_token_returns_string() -> None:
    token = create_user_token(
        user_id="123",
        email="vincent@example.com",
    )

    assert isinstance(token, str)


def test_create_user_token_contains_user_id() -> None:
    token = create_user_token(
        user_id="123",
        email="vincent@example.com",
    )

    payload = decode_access_token(token)

    assert payload["sub"] == "123"


def test_create_user_token_contains_email() -> None:
    token = create_user_token(
        user_id="123",
        email="vincent@example.com",
    )

    payload = decode_access_token(token)

    assert payload["email"] == "vincent@example.com"