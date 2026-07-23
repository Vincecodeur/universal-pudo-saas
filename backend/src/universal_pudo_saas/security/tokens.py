from datetime import UTC
from datetime import datetime
from datetime import timedelta

from jose import jwt


SECRET_KEY = "CHANGE_ME_IN_SETTINGS"
ALGORITHM = "HS256"


def create_access_token(
    subject: str,
    email: str,
    expires_delta: timedelta | None = None,
) -> str:
    if expires_delta is None:
        expires_delta = timedelta(minutes=60)

    expire = datetime.now(UTC) + expires_delta

    payload = {
        "sub": subject,
        "email": email,
        "exp": expire,
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )


def decode_access_token(
    token: str,
) -> dict:
    return jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM],
    )