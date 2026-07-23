from universal_pudo_saas.security.tokens import (
    create_access_token,
    decode_access_token,
)


def test_create_access_token_returns_string() -> None:
    token = create_access_token(
        subject="123",
        email="vincent@example.com",
    )

    assert isinstance(token, str)


def test_decode_access_token_returns_payload() -> None:
    token = create_access_token(
        subject="123",
        email="vincent@example.com",
    )

    payload = decode_access_token(token)

    assert payload["sub"] == "123"


def test_token_contains_email() -> None:
    token = create_access_token(
        subject="123",
        email="vincent@example.com",
    )

    payload = decode_access_token(token)

    assert payload["email"] == "vincent@example.com"


def test_tokens_are_generated() -> None:
    token = create_access_token(
        subject="123",
        email="vincent@example.com",
    )

    assert len(token) > 0