import pytest
from typing import Any
from src.Category import Category
from src.Products import Product


@pytest.fixture
def prod_1() -> Any:
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def prod_2() -> Any:
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def prod_3() -> Any:
    return Product("Iphone 16", "1TB, White", 250000.0, 2)


@pytest.fixture
def category(prod_1: Product, prod_2: Product) -> Any:
    return Category("Смартфоны", "Смартфоны, как средство не только коммуникации, "
                                 "но и получение дополнительных функций для удобства жизни", [prod_1, prod_2])


@pytest.fixture
def new_product() -> Any:
    return Product.new_product(
        {"name": "Samsung Galaxy S24 Ultra", "description": "516GB, Белый цвет, 250MP камера", "price": 200000.0,
         "quantity": 4})
