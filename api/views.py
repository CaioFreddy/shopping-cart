from .models import Cart, Product
from . import controllers
from fastapi import APIRouter
from typing import List

router = APIRouter()


@router.get("/cart/{client_name}", response_model=Cart)
async def view_cart(client_name: str):
    cart = controllers.get_cart(client_name)
    return cart


@router.post("/cart/{client_name}", response_model=Cart)
async def update_cart(client_name: str, products: List[Product]):
    cart = controllers.update_cart(client_name, products)
    return cart
