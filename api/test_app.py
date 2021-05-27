from fastapi.applications import FastAPI
from .views import router
from fastapi import FastAPI
from .models import Client, Cart
from fastapi.testclient import TestClient
from unittest import mock


class Redis:
    def __init__(self, *args, **kwargs):
        self.cliente = Cart(client=Client(name='Test'),
                            products=[], total=0).json()

    def get(self, *args, **kwargs):
        return self.cliente


app = FastAPI()

app.include_router(router)

client = TestClient(app)


@mock.patch('redis.Redis', side_effect=Redis)
def test_read_main(mock_redis):
    response = client.get("/cart/caio")
    assert response.status_code == 200
    assert response.json() == {'client': {'name': 'Test'},
                               'products': [], 'total': 0.0}
