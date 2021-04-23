from .models import Cart, Client, Product
from typing import List


def get_cart(client_name):
    return Cart(client=Client(name=client_name),
                products=[Product(name='PS5', price='5000.00',
                                      quantity=2)],
                total=sum(
                    map(lambda x: x.price * x.quantity,
                        [Product(name='PS5', price='5000.00',
                                     quantity=2)])))


def update_cart(client_name):
    return Cart(client=Client(name=client_name),
                products=List[Product(name='PS5', price='5000.00',
                                      quantity=1)],
                total=sum(
                    map(lambda x: x.price * x.quantity,
                        List[Product(name='PS5', price='5000.00',
                                     quantity=1)])))
