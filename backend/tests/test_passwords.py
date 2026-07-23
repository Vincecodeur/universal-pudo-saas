from universal_pudo_saas.security.passwords import (
    hash_password,
    verify_password,
)


def test_hash_password_returns_different_value() -> None:
    password = "secret123"

    password_hash = hash_password(password)

    assert password_hash != password


def test_hash_password_returns_string() -> None:
    password_hash = hash_password("secret123")

    assert isinstance(password_hash, str)


def test_hash_password_is_not_empty() -> None:
    password_hash = hash_password("secret123")

    assert len(password_hash) > 0


def test_verify_password_success() -> None:
    password_hash = hash_password("secret123")

    assert verify_password(
        "secret123",
        password_hash,
    )


def test_verify_password_failure() -> None:
    password_hash = hash_password("secret123")

    assert not verify_password(
        "wrong-password",
        password_hash,
    )


def test_same_password_generates_different_hashes() -> None:
    password = "secret123"

    hash_1 = hash_password(password)
    hash_2 = hash_password(password)

    assert hash_1 != hash_2


def test_both_hashes_validate_same_password() -> None:
    password = "secret123"

    hash_1 = hash_password(password)
    hash_2 = hash_password(password)

    assert verify_password(password, hash_1)
    assert verify_password(password, hash_2)