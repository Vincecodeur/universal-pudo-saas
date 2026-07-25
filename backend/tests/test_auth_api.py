from fastapi.testclient import TestClient

from universal_pudo_saas.main import app

client = TestClient(app)


def test_login_endpoint_exists() -> None:
    response = client.post(
        "/auth/login",
        json={
            "email": "user@example.com",
            "password": "secret123",
        },
    )

    assert response.status_code == 200


def test_login_returns_token() -> None:
    response = client.post(
        "/auth/login",
        json={
            "email": "user@example.com",
            "password": "secret123",
        },
    )

    payload = response.json()

    assert "access_token" in payload
    assert payload["token_type"] == "bearer"


def test_login_invalid_password() -> None:
    response = client.post(
        "/auth/login",
        json={
            "email": "user@example.com",
            "password": "wrong-password",
        },
    )

    assert response.status_code == 401


def test_login_invalid_email() -> None:
    response = client.post(
        "/auth/login",
        json={
            "email": "unknown@example.com",
            "password": "secret123",
        },
    )

    assert response.status_code == 401


def test_login_returns_real_jwt() -> None:
    response = client.post(
        "/auth/login",
        json={
            "email": "user@example.com",
            "password": "secret123",
        },
    )

    payload = response.json()

    token = payload["access_token"]

    assert len(token) > 50


def test_me_requires_authorization_header() -> None:
    response = client.get("/auth/me")

    assert response.status_code == 401


def test_me_returns_current_user() -> None:
    login_response = client.post(
        "/auth/login",
        json={
            "email": "user@example.com",
            "password": "secret123",
        },
    )

    token = login_response.json()["access_token"]

    response = client.get(
        "/auth/me",
        headers={
            "Authorization": f"Bearer {token}",
        },
    )

    assert response.status_code == 200

    payload = response.json()

    assert payload["user_id"] == "user-001"
    assert payload["email"] == "user@example.com"