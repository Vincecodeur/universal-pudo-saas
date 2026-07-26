from __future__ import annotations

from typing import Protocol

from universal_pudo_saas.engine_catalog.models import (
    Carrier,
)


class EngineCatalogClient(Protocol):
    """
    Contract used by the SaaS to consume the Engine carrier catalogue.

    This protocol represents the expected client behavior.

    Concrete implementations may later use:
    - direct Python package calls
    - HTTP API calls
    - SDK calls

    For now, no real Engine call is implemented.
    """

    def list_carriers(
        self,
    ) -> list[Carrier]:
        ...

    def get_carrier(
        self,
        carrier_id: str,
    ) -> Carrier | None:
        ...


class InMemoryEngineCatalogClient:
    """
    In-memory implementation used for the SaaS foundation and tests.

    This client does not call Universal PUDO Engine.

    It allows the SaaS service layer to be implemented and tested before
    deciding the final runtime integration mechanism.
    """

    def __init__(
        self,
        carriers: list[Carrier] | None = None,
    ) -> None:
        self._carriers = carriers or []

    def list_carriers(
        self,
    ) -> list[Carrier]:
        return list(self._carriers)

    def get_carrier(
        self,
        carrier_id: str,
    ) -> Carrier | None:
        for carrier in self._carriers:
            if carrier.carrier_id == carrier_id:
                return carrier

        return None