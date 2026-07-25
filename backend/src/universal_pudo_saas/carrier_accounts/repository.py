from __future__ import annotations

import uuid

from universal_pudo_saas.carrier_accounts.models import (
    CarrierAccount,
)
from universal_pudo_saas.database.session import (
    SessionLocal,
)


def get_carrier_account(
    carrier_account_id: uuid.UUID,
) -> CarrierAccount | None:
    session = SessionLocal()

    try:
        return session.get(
            CarrierAccount,
            carrier_account_id,
        )
    finally:
        session.close()


def list_carrier_accounts_by_organisation(
    organisation_id: uuid.UUID,
) -> list[CarrierAccount]:
    
    session = SessionLocal()

    try:
        return (
            session.query(CarrierAccount)
            .filter(
                CarrierAccount.organisation_id
                == organisation_id
            )
            .all()
        )
    finally:
        session.close()