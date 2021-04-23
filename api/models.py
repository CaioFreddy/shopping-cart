from typing import Optional, List

from pydantic import BaseModel


class Product(BaseModel):
    name: str
    price: float
    quantity: int


class Client(BaseModel):
    name: str


class Cart(BaseModel):
    client: Client
    products: List[Product]
    total: float