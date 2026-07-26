from __future__ import annotations

from sqlalchemy.orm import Session

from universal_pudo_saas.carrier_credentials.models import (
    CarrierCredential,
)
from universal_pudo_saas.carrier_credentials.repository import (
    get_carrier_credential,
    list_credentials_by_carrier_account,
)


def get_carrier_credential_service(
    session: Session,
    carrier_credential_id,
) -> CarrierCredential | None:
    return get_carrier_credential(
        carrier_credential_id,
    )


def list_credentials_for_carrier_account(
    session: Session,
    carrier_account_id,
) -> list[CarrierCredential]:
    return list_credentials_by_carrier_account(
        carrier_account_id,
)