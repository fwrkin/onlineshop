import pytest

from classes.Product import Product


@pytest.fixture
def product() -> "Product":
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_init(product: Product) -> None:
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_new_product(product: Product) -> None:
    new_dict = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
    ret = product.new_product(new_dict)
    assert ret.name == "Samsung Galaxy S23 Ultra"


def test_price(product: Product) -> None:
    assert product.price == 180000.0
    product.price = 50
    assert product.price == 50
    product.price = -50
    assert product.price == 50
