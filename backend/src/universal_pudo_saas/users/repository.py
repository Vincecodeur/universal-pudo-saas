from __future__ import annotations

from dataclasses import dataclass

from universal_pudo_saas.security.passwords import (
    hash_password,
)


@dataclass
class UserRecord:
    id: str
    email: str
    password_hash: str


def find_user_by_email(
    email: str,
) -> UserRecord | None:
    if email != "user@example.com":
        return None

    return UserRecord(
        id="user-001",
        email="user@example.com",
        password_hash=hash_password(
            "secret123",
        ),
    )