import pytest

from fastapi.testclient import TestClient

from main import app


@pytest.fixture
def client() -> TestClient:
    test_app = TestClient(app)
    return test_app
