from universal_pudo_saas.security.passwords import verify_password
from universal_pudo_saas.security.tokens import create_access_token


def authenticate_user(
    plain_password: str,
    password_hash: str,
) -> bool:
    return verify_password(
        plain_password,
        password_hash,
    )


def create_user_token(
    user_id: str,
    email: str,
) -> str:
    return create_access_token(
        subject=user_id,
        email=email,
    )