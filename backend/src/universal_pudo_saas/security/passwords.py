from passlib.context import CryptContext


pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
)


def hash_password(password: str) -> str:
    """
    Generate a bcrypt hash for a plaintext password.
    """
    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    password_hash: str,
) -> bool:
    """
    Verify a plaintext password against an existing bcrypt hash.
    """
    return pwd_context.verify(
        plain_password,
        password_hash,
    )