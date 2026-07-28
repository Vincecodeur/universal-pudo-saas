from datetime import timezone
from uuid import UUID, uuid4

from universal_pudo_saas.search_platform.models import (
    SearchExecutionMetadata,
    SearchRequest,
    SearchResult,
)


def test_search_request_creation() -> None:
    organisation_id = uuid4()

    request = SearchRequest(
        organisation_id=organisation_id,
        query="Paris",
        country_code="FR",
        postal_code="75001",
        city="Paris",
        latitude=48.8566,
        longitude=2.3522,
        radius_km=10,
        carrier_codes=["MONDIAL_RELAY"],
        limit=50,
    )

    assert request.organisation_id == organisation_id
    assert request.query == "Paris"
    assert request.country_code == "FR"
    assert request.postal_code == "75001"
    assert request.city == "Paris"
    assert request.latitude == 48.8566
    assert request.longitude == 2.3522
    assert request.radius_km == 10
    assert request.carrier_codes == ["MONDIAL_RELAY"]
    assert request.limit == 50


def test_search_request_defaults() -> None:
    request = SearchRequest(
        organisation_id=uuid4(),
    )

    assert request.query is None
    assert request.country_code is None
    assert request.postal_code is None
    assert request.city is None
    assert request.latitude is None
    assert request.longitude is None
    assert request.radius_km is None
    assert request.carrier_codes == []
    assert request.limit == 100


def test_search_execution_metadata_defaults() -> None:
    metadata = SearchExecutionMetadata()

    assert isinstance(metadata.search_id, UUID)
    assert metadata.executed_at.tzinfo == timezone.utc
    assert metadata.duration_ms == 0
    assert metadata.source == "search_platform"
    assert metadata.applied_filters == []


def test_search_execution_metadata_creation() -> None:
    search_id = uuid4()

    metadata = SearchExecutionMetadata(
        search_id=search_id,
        duration_ms=42,
        source="unit_test",
        applied_filters=[
            "country_code",
            "postal_code",
        ],
    )

    assert metadata.search_id == search_id
    assert metadata.duration_ms == 42
    assert metadata.source == "unit_test"
    assert metadata.applied_filters == [
        "country_code",
        "postal_code",
    ]


def test_search_result_creation() -> None:
    metadata = SearchExecutionMetadata(
        duration_ms=15,
        applied_filters=[
            "country_code",
            "postal_code",
        ],
    )

    result = SearchResult(
        pickup_points=[],
        total_results=2,
        executed_carriers=[
            "MONDIAL_RELAY",
            "COLISSIMO",
        ],
        failed_carriers=[
            "UPS",
        ],
        metadata=metadata,
    )

    assert result.pickup_points == []
    assert result.total_results == 2
    assert result.executed_carriers == [
        "MONDIAL_RELAY",
        "COLISSIMO",
    ]
    assert result.failed_carriers == ["UPS"]
    assert result.metadata == metadata


def test_search_result_defaults() -> None:
    result = SearchResult(
        pickup_points=[],
        total_results=0,
    )

    assert result.pickup_points == []
    assert result.total_results == 0
    assert result.executed_carriers == []
    assert result.failed_carriers == []
    assert isinstance(result.metadata, SearchExecutionMetadata)


def test_search_request_lists_are_independent() -> None:
    request_a = SearchRequest(
        organisation_id=uuid4(),
    )

    request_b = SearchRequest(
        organisation_id=uuid4(),
    )

    request_a.carrier_codes.append("MONDIAL_RELAY")

    assert request_a.carrier_codes == ["MONDIAL_RELAY"]
    assert request_b.carrier_codes == []


def test_search_result_lists_are_independent() -> None:
    result_a = SearchResult(
        pickup_points=[],
        total_results=0,
    )

    result_b = SearchResult(
        pickup_points=[],
        total_results=0,
    )

    result_a.executed_carriers.append("COLISSIMO")
    result_a.failed_carriers.append("UPS")

    assert result_a.executed_carriers == ["COLISSIMO"]
    assert result_a.failed_carriers == ["UPS"]
    assert result_b.executed_carriers == []
    assert result_b.failed_carriers == []


def test_search_execution_metadata_lists_are_independent() -> None:
    metadata_a = SearchExecutionMetadata()
    metadata_b = SearchExecutionMetadata()

    metadata_a.applied_filters.append("city")

    assert metadata_a.applied_filters == ["city"]
    assert metadata_b.applied_filters == []
