from __future__ import annotations

import uuid

from universal_pudo_saas.carrier_credentials.models import (
    CarrierCredential,
)
from universal_pudo_saas.database.session import (
    SessionLocal,
)


def get_carrier_credential(
    credential_id: uuid.UUID,
) -> CarrierCredential | None:
    session = SessionLocal()

    try:
        return session.get(
            CarrierCredential,
            credential_id,
        )
    finally:
        session.close()


def list_credentials_by_carrier_account(
    carrier_account_id: uuid.UUID,
) -> list[CarrierCredential]:
    session = SessionLocal()

    try:
        return (
            session.query(CarrierCredential)
            .filter(
                CarrierCredential.carrier_account_id
                == carrier_account_id
            )
            .all()
        )
    finally:
        session.close()