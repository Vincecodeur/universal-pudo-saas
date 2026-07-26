from __future__ import annotations

import uuid

from universal_pudo_saas.carrier_accounts.models import (
    CarrierAccount,
)
from universal_pudo_saas.carrier_catalog.service import (
    CarrierCatalogService,
)
from universal_pudo_saas.database.session import (
    SessionLocal,
)
from universal_pudo_saas.engine_catalog.client import (
    InMemoryEngineCatalogClient,
)
from universal_pudo_saas.engine_catalog.models import (
    Carrier,
    CarrierLifecycle,
)
from universal_pudo_saas.engine_catalog.service import (
    EngineCatalogService,
)
from universal_pudo_saas.organisations.models import (
    Organisation,
)


def build_engine_catalog_service() -> EngineCatalogService:
    carriers = [
        Carrier(
            carrier_id="active",
            code="COLISSIMO",
            name="Colissimo",
            lifecycle=CarrierLifecycle.ACTIVE,
        ),
        Carrier(
            carrier_id="deprecated",
            code="MR",
            name="Mondial Relay",
            lifecycle=CarrierLifecycle.DEPRECATED,
        ),
        Carrier(
            carrier_id="sunset",
            code="CHRONOPOST",
            name="Chronopost",
            lifecycle=CarrierLifecycle.SUNSET,
        ),
        Carrier(
            carrier_id="removed",
            code="REM",
            name="Removed Carrier",
            lifecycle=CarrierLifecycle.REMOVED,
        ),
    ]

    return EngineCatalogService(
        InMemoryEngineCatalogClient(
            carriers=carriers,
        ),
    )


def build_carrier_catalog_service() -> CarrierCatalogService:
    return CarrierCatalogService(
        engine_catalog_service=build_engine_catalog_service(),
    )


def test_list_available_carriers_returns_visible_engine_carriers() -> None:
    service = build_carrier_catalog_service()

    result = service.list_available_carriers()

    carrier_ids = {
        carrier.carrier_id
        for carrier in result
    }

    assert carrier_ids == {
        "active",
        "deprecated",
        "sunset",
    }


def test_list_organisation_carriers_returns_matching_engine_carriers() -> None:
    session = SessionLocal()

    organisation = None
    account_1 = None
    account_2 = None

    try:
        organisation = Organisation(
            name="Carrier Catalog Organisation",
        )

        session.add(organisation)
        session.commit()
        session.refresh(organisation)

        account_1 = CarrierAccount(
            organisation_id=organisation.id,
            carrier_code="COLISSIMO",
            name="Colissimo Account",
        )

        account_2 = CarrierAccount(
            organisation_id=organisation.id,
            carrier_code="MR",
            name="Mondial Relay Account",
        )

        session.add(account_1)
        session.add(account_2)
        session.commit()

        service = build_carrier_catalog_service()

        result = service.list_organisation_carriers(
            organisation_id=organisation.id,
        )

        carrier_codes = {
            carrier.code
            for carrier in result
        }

        assert carrier_codes == {
            "COLISSIMO",
            "MR",
        }

    finally:
        if account_1 is not None:
            session.delete(account_1)

        if account_2 is not None:
            session.delete(account_2)

        if organisation is not None:
            session.delete(organisation)

        session.commit()
        session.close()


def test_list_organisation_carriers_returns_empty_list_when_no_account_exists() -> None:
    service = build_carrier_catalog_service()

    result = service.list_organisation_carriers(
        organisation_id=uuid.uuid4(),
    )

    assert result == []


def test_list_activatable_carriers_for_organisation_excludes_existing_accounts() -> None:
    session = SessionLocal()

    organisation = None
    account = None

    try:
        organisation = Organisation(
            name="Carrier Catalog Activatable Organisation",
        )

        session.add(organisation)
        session.commit()
        session.refresh(organisation)

        account = CarrierAccount(
            organisation_id=organisation.id,
            carrier_code="COLISSIMO",
            name="Colissimo Account",
        )

        session.add(account)
        session.commit()

        service = build_carrier_catalog_service()

        result = service.list_activatable_carriers_for_organisation(
            organisation_id=organisation.id,
        )

        carrier_codes = {
            carrier.code
            for carrier in result
        }

        assert carrier_codes == {
            "MR",
        }

    finally:
        if account is not None:
            session.delete(account)

        if organisation is not None:
            session.delete(organisation)

        session.commit()
        session.close()


def test_list_activatable_carriers_for_organisation_returns_empty_list_when_all_activatable_carriers_exist() -> None:
    session = SessionLocal()

    organisation = None
    account_1 = None
    account_2 = None

    try:
        organisation = Organisation(
            name="Carrier Catalog Full Organisation",
        )

        session.add(organisation)
        session.commit()
        session.refresh(organisation)

        account_1 = CarrierAccount(
            organisation_id=organisation.id,
            carrier_code="COLISSIMO",
            name="Colissimo Account",
        )

        account_2 = CarrierAccount(
            organisation_id=organisation.id,
            carrier_code="MR",
            name="Mondial Relay Account",
        )

        session.add(account_1)
        session.add(account_2)
        session.commit()

        service = build_carrier_catalog_service()

        result = service.list_activatable_carriers_for_organisation(
            organisation_id=organisation.id,
        )

        assert result == []

    finally:
        if account_1 is not None:
            session.delete(account_1)

        if account_2 is not None:
            session.delete(account_2)

        if organisation is not None:
            session.delete(organisation)

        session.commit()
        session.close()