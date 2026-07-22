from fastapi.testclient import TestClient

from universal_pudo_saas.main import create_app


def test_health_endpoint_returns_ok() -> None:
    client = TestClient(
        create_app()
    )

    response = client.get(
        "/health"
    )

    assert response.status_code == 200

    assert response.json() == {
        "status": "ok",
        "service": "Universal PUDO SaaS",
        "environment": "development",
    }
