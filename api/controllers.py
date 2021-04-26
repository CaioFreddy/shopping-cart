import json

from .models import Cart, Client, Product
from .redis import instance_redis
from typing import List


def get_cart(client_name):
    redis = instance_redis()
    cart = redis.get(client_name)
    return json.loads(cart) if cart else None


def update_cart(client_name, products=[]):
    cart = Cart(client=Client(name=client_name),
                products=products,
                total=sum(map(lambda x: x.price * x.quantity, products)))
    redis = instance_redis()
    redis.set(client_name, cart.json())
    return cart
