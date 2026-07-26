from __future__ import annotations

import uuid

from fastapi import APIRouter
from fastapi import HTTPException

from universal_pudo_saas.carrier_accounts.service import (
    get_carrier_account_service,
    list_carrier_accounts_for_organisation,
)
from universal_pudo_saas.database.session import (
    SessionLocal,
)

router = APIRouter(
    prefix="/carrier-accounts",
    tags=["carrier-accounts"],
)


@router.get("/organisation/{organisation_id}")
def get_organisation_carrier_accounts(
    organisation_id: uuid.UUID,
):
    session = SessionLocal()

    try:
        return list_carrier_accounts_for_organisation(
            session=session,
            organisation_id=organisation_id,
        )

    finally:
        session.close()

@router.get("/{carrier_account_id}")
def get_carrier_account(
    carrier_account_id: uuid.UUID,
):
    session = SessionLocal()

    try:
        carrier_account = get_carrier_account_service(
            session=session,
            carrier_account_id=carrier_account_id,
        )

        if carrier_account is None:
            raise HTTPException(
                status_code=404,
                detail="Carrier account not found",
            )

        return carrier_account

    finally:
        session.close()


