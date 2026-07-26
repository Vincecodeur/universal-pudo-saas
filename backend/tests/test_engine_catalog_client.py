from universal_pudo_saas.engine_catalog.client import (
    InMemoryEngineCatalogClient,
)
from universal_pudo_saas.engine_catalog.models import (
    Carrier,
)


def test_list_carriers_returns_all_carriers() -> None:
    carrier_1 = Carrier(
        carrier_id="carrier-1",
        code="COLISSIMO",
        name="Colissimo",
    )

    carrier_2 = Carrier(
        carrier_id="carrier-2",
        code="MR",
        name="Mondial Relay",
    )

    client = InMemoryEngineCatalogClient(
        carriers=[
            carrier_1,
            carrier_2,
        ],
    )

    result = client.list_carriers()

    assert len(result) == 2
    assert carrier_1 in result
    assert carrier_2 in result


def test_get_carrier_returns_matching_carrier() -> None:
    carrier = Carrier(
        carrier_id="carrier-1",
        code="COLISSIMO",
        name="Colissimo",
    )

    client = InMemoryEngineCatalogClient(
        carriers=[carrier],
    )

    result = client.get_carrier("carrier-1")

    assert result == carrier


def test_get_carrier_returns_none_when_not_found() -> None:
    client = InMemoryEngineCatalogClient()

    result = client.get_carrier("unknown")

    assert result is None


def test_list_carriers_returns_copy_of_collection() -> None:
    carrier = Carrier(
        carrier_id="carrier-1",
        code="COLISSIMO",
        name="Colissimo",
    )

    client = InMemoryEngineCatalogClient(
        carriers=[carrier],
    )

    result = client.list_carriers()

    result.clear()

    assert len(client.list_carriers()) == 1
