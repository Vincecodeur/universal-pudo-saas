from __future__ import annotations

import uuid

from fastapi import APIRouter
from fastapi import HTTPException

from universal_pudo_saas.carrier_credentials.service import (
    get_carrier_credential_service,
    list_credentials_for_carrier_account,
)
from universal_pudo_saas.database.session import (
    SessionLocal,
)

router = APIRouter(
    prefix="/carrier-credentials",
    tags=["carrier-credentials"],
)

@router.get("/carrier-account/{carrier_account_id}")
def get_carrier_account_credentials(
    carrier_account_id: uuid.UUID,
):
    session = SessionLocal()

    try:
        return list_credentials_for_carrier_account(
            session=session,
            carrier_account_id=carrier_account_id,
        )

    finally:
        session.close()

@router.get("/{carrier_credential_id}")
def get_carrier_credential(
    carrier_credential_id: uuid.UUID,
):
    session = SessionLocal()

    try:
        credential = get_carrier_credential_service(
            session=session,
            carrier_credential_id=carrier_credential_id,
        )

        if credential is None:
            raise HTTPException(
                status_code=404,
                detail="Carrier credential not found",
            )

        return credential

    finally:
        session.close()


