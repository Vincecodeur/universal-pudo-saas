from __future__ import annotations

from fastapi import APIRouter
from fastapi import Header
from fastapi import HTTPException

from universal_pudo_saas.auth.schemas import (
    CurrentUserResponse,
    LoginRequest,
    LoginResponse,
)
from universal_pudo_saas.auth.service import (
    authenticate_user,
    create_user_token,
)
from universal_pudo_saas.security.tokens import (
    decode_access_token,
)
from universal_pudo_saas.users.repository import (
    find_user_by_email,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/login",
    response_model=LoginResponse,
)
def login(
    payload: LoginRequest,
) -> LoginResponse:
    user = find_user_by_email(
        payload.email,
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
        )

    if not authenticate_user(
        payload.password,
        user.password_hash,
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
        )

    token = create_user_token(
        user_id=user.id,
        email=user.email,
    )

    return LoginResponse(
        access_token=token,
    )


@router.get(
    "/me",
    response_model=CurrentUserResponse,
)
def me(
    authorization: str | None = Header(
        default=None,
    ),
) -> CurrentUserResponse:
    if authorization is None:
        raise HTTPException(
            status_code=401,
            detail="Missing authorization header",
        )

    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Invalid authorization header",
        )

    token = authorization.removeprefix(
        "Bearer ",
    )

    try:
        payload = decode_access_token(
            token,
        )
    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid token",
        )

    return CurrentUserResponse(
        user_id=payload["sub"],
        email=payload["email"],
    )