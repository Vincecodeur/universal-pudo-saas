from universal_pudo_saas.map_service.models import (
    MapCenter,
    MapMarker,
    MapPopup,
    MapProjectionResult,
    MapViewState,
)


def test_map_center_stores_coordinates() -> None:
    center = MapCenter(latitude=48.8566, longitude=2.3522)

    assert center.latitude == 48.8566
    assert center.longitude == 2.3522


def test_map_view_state_defaults_are_isolated() -> None:
    first_state = MapViewState()
    second_state = MapViewState()

    first_state.visible_carriers.append("COLISSIMO")

    assert first_state.visible_carriers == ["COLISSIMO"]
    assert second_state.visible_carriers == []


def test_map_marker_represents_presentation_projection() -> None:
    marker = MapMarker(
        pickup_point_id="pickup-1",
        latitude=48.8566,
        longitude=2.3522,
        carrier_code="COLISSIMO",
        carrier_display_name="Colissimo",
        carrier_logo_url="https://example.test/logo.png",
        carrier_color="#1A73E8",
    )

    assert marker.pickup_point_id == "pickup-1"
    assert marker.latitude == 48.8566
    assert marker.longitude == 2.3522
    assert marker.carrier_code == "COLISSIMO"
    assert marker.carrier_display_name == "Colissimo"
    assert marker.carrier_logo_url == "https://example.test/logo.png"
    assert marker.carrier_color == "#1A73E8"


def test_map_popup_represents_marker_details() -> None:
    popup = MapPopup(
        pickup_point_id="pickup-1",
        pickup_point_name="Pickup Point Paris",
        carrier="COLISSIMO",
        address="10 Rue Test, 75001 Paris, France",
        distance=1.2,
        opening_hours={"monday": "09:00-18:00"},
        details_link="/pickup-points/pickup-1",
    )

    assert popup.pickup_point_id == "pickup-1"
    assert popup.pickup_point_name == "Pickup Point Paris"
    assert popup.carrier == "COLISSIMO"
    assert popup.address == "10 Rue Test, 75001 Paris, France"
    assert popup.distance == 1.2
    assert popup.opening_hours == {"monday": "09:00-18:00"}
    assert popup.details_link == "/pickup-points/pickup-1"


def test_map_projection_result_defaults_are_isolated() -> None:
    first_result = MapProjectionResult()
    second_result = MapProjectionResult()

    first_result.markers.append(
        MapMarker(
            pickup_point_id="pickup-1",
            latitude=48.8566,
            longitude=2.3522,
            carrier_code="COLISSIMO",
        )
    )

    assert len(first_result.markers) == 1
    assert second_result.markers == []
    assert first_result.popups == {}
    assert second_result.popups == {}