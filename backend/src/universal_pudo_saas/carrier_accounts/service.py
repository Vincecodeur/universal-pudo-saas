from __future__ import annotations

from sqlalchemy.orm import Session

from universal_pudo_saas.carrier_accounts.models import (
    CarrierAccount,
)
from universal_pudo_saas.carrier_accounts.repository import (
    get_carrier_account,
    list_carrier_accounts_by_organisation,
)


def create_carrier_account(
    session: Session,
    organisation_id,
    carrier_code: str,
    name: str,
) -> CarrierAccount:
    if not organisation_id:
        raise ValueError("organisation_id is required")

    if not carrier_code:
        raise ValueError("carrier_code is required")

    if not name:
        raise ValueError("name is required")

    carrier_account = CarrierAccount(
        organisation_id=organisation_id,
        carrier_code=carrier_code,
        name=name,
    )

    session.add(carrier_account)
    session.commit()
    session.refresh(carrier_account)

    return carrier_account


def get_carrier_account_service(
    session: Session,
    carrier_account_id,
) -> CarrierAccount | None:
    return get_carrier_account(
        carrier_account_id,
    )


def list_carrier_accounts_for_organisation(
    session: Session,
    organisation_id,
) -> list[CarrierAccount]:
    return list_carrier_accounts_by_organisation(
    organisation_id,
)