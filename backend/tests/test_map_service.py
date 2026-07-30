from types import SimpleNamespace

import pytest

from universal_pudo_saas.map_service.models import MapProjectionResult
from universal_pudo_saas.map_service.service import MapService


def make_pickup_point(
    pickup_point_id: str = "pickup-1",
    carrier_code: str = "COLISSIMO",
    latitude: float = 48.8566,
    longitude: float = 2.3522,
) -> SimpleNamespace:
    return SimpleNamespace(
        id=pickup_point_id,
        carrier_code=carrier_code,
        name="Pickup Point Paris",
        location=SimpleNamespace(
            latitude=latitude,
            longitude=longitude,
        ),
        address=SimpleNamespace(
            line1="10 Rue Test",
            postal_code="75001",
            city="Paris",
            country="France",
        ),
        distance=1.2,
        opening_hours={"monday": "09:00-18:00"},
        details_link=f"/pickup-points/{pickup_point_id}",
    )


def make_search_result(pickup_points: list[SimpleNamespace]) -> SimpleNamespace:
    return SimpleNamespace(
        pickup_points=pickup_points,
        total_results=len(pickup_points),
        executed_carriers=["COLISSIMO", "MONDIAL_RELAY"],
        failed_carriers=[],
        metadata=SimpleNamespace(search_id="search-1"),
    )


def test_create_marker_projection_from_pickup_point() -> None:
    service = MapService()
    pickup_point = make_pickup_point()

    marker = service.create_marker_projection(
        pickup_point=pickup_point,
        branding={
            "display_name": "Colissimo",
            "logo_url": "https://example.test/colissimo.png",
            "color": "#1A73E8",
        },
    )

    assert marker.pickup_point_id == "pickup-1"
    assert marker.latitude == 48.8566
    assert marker.longitude == 2.3522
    assert marker.carrier_code == "COLISSIMO"
    assert marker.carrier_display_name == "Colissimo"
    assert marker.carrier_logo_url == "https://example.test/colissimo.png"
    assert marker.carrier_color == "#1A73E8"


def test_create_marker_projection_uses_carrier_code_as_default_display_name() -> None:
    service = MapService()
    pickup_point = make_pickup_point(carrier_code="MONDIAL_RELAY")

    marker = service.create_marker_projection(pickup_point=pickup_point)

    assert marker.carrier_code == "MONDIAL_RELAY"
    assert marker.carrier_display_name == "MONDIAL_RELAY"


def test_create_popup_projection_from_pickup_point() -> None:
    service = MapService()
    pickup_point = make_pickup_point()

    popup = service.create_popup_projection(pickup_point=pickup_point)

    assert popup.pickup_point_id == "pickup-1"
    assert popup.pickup_point_name == "Pickup Point Paris"
    assert popup.carrier == "COLISSIMO"
    assert popup.address == "10 Rue Test, 75001, Paris, France"
    assert popup.distance == 1.2
    assert popup.opening_hours == {"monday": "09:00-18:00"}
    assert popup.details_link == "/pickup-points/pickup-1"


def test_build_map_projection_from_search_result() -> None:
    service = MapService()

    pickup_points = [
        make_pickup_point(pickup_point_id="pickup-1", carrier_code="COLISSIMO"),
        make_pickup_point(pickup_point_id="pickup-2", carrier_code="MONDIAL_RELAY"),
    ]
    search_result = make_search_result(pickup_points)

    projection = service.build_map_projection(search_result=search_result)

    assert isinstance(projection, MapProjectionResult)
    assert projection.total_markers == 2
    assert len(projection.markers) == 2
    assert set(projection.popups.keys()) == {"pickup-1", "pickup-2"}
    assert projection.executed_carriers == ["COLISSIMO", "MONDIAL_RELAY"]
    assert projection.failed_carriers == []


def test_build_map_projection_filters_visible_carriers() -> None:
    service = MapService()

    pickup_points = [
        make_pickup_point(pickup_point_id="pickup-1", carrier_code="COLISSIMO"),
        make_pickup_point(pickup_point_id="pickup-2", carrier_code="MONDIAL_RELAY"),
    ]
    search_result = make_search_result(pickup_points)

    projection = service.build_map_projection(
        search_result=search_result,
        visible_carriers=["COLISSIMO"],
    )

    assert projection.total_markers == 1
    assert projection.markers[0].pickup_point_id == "pickup-1"
    assert projection.markers[0].carrier_code == "COLISSIMO"
    assert projection.view_state.visible_carriers == ["COLISSIMO"]


def test_build_map_projection_keeps_valid_selected_pickup_point() -> None:
    service = MapService()

    pickup_points = [
        make_pickup_point(pickup_point_id="pickup-1", carrier_code="COLISSIMO"),
    ]
    search_result = make_search_result(pickup_points)

    projection = service.build_map_projection(
        search_result=search_result,
        selected_pickup_point_id="pickup-1",
    )

    assert projection.view_state.selected_pickup_point_id == "pickup-1"


def test_build_map_projection_resets_invalid_selected_pickup_point() -> None:
    service = MapService()

    pickup_points = [
        make_pickup_point(pickup_point_id="pickup-1", carrier_code="COLISSIMO"),
    ]
    search_result = make_search_result(pickup_points)

    projection = service.build_map_projection(
        search_result=search_result,
        selected_pickup_point_id="unknown-pickup",
    )

    assert projection.view_state.selected_pickup_point_id is None


def test_build_map_projection_does_not_mutate_search_result() -> None:
    service = MapService()

    pickup_points = [
        make_pickup_point(pickup_point_id="pickup-1", carrier_code="COLISSIMO"),
    ]
    search_result = make_search_result(pickup_points)

    service.build_map_projection(search_result=search_result)

    assert search_result.pickup_points == pickup_points
    assert search_result.total_results == 1
    assert search_result.executed_carriers == ["COLISSIMO", "MONDIAL_RELAY"]


def test_marker_projection_requires_pickup_point_id() -> None:
    service = MapService()

    pickup_point = make_pickup_point()
    pickup_point.id = None
    pickup_point.pickup_point_id = None
    pickup_point.code = None

    with pytest.raises(ValueError, match="Pickup point id is required"):
        service.create_marker_projection(pickup_point=pickup_point)


def test_marker_projection_requires_coordinates() -> None:
    service = MapService()

    pickup_point = make_pickup_point()
    pickup_point.location = None
    pickup_point.latitude = None
    pickup_point.longitude = None

    with pytest.raises(ValueError, match="Latitude and longitude are required"):
        service.create_marker_projection(pickup_point=pickup_point)


def test_marker_projection_requires_carrier_code() -> None:
    service = MapService()

    pickup_point = make_pickup_point()
    pickup_point.carrier_code = None
    pickup_point.carrier = None

    with pytest.raises(ValueError, match="Carrier code is required"):
        service.create_marker_projection(pickup_point=pickup_point)