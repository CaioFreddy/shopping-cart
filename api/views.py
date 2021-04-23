from .models import Cart
from . import controllers
from fastapi import APIRouter

router = APIRouter()


@router.get("/cart/{client_name}", response_model=Cart)
async def view_cart(client_name: str):
    cart = controllers.get_cart(client_name)
    return cart


@router.put("/cart/{client_name}", response_model=Cart)
async def update_cart(client_name: str):
    cart = controllers.update_cart(client_name)
    return cart
