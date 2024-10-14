import pytest
from typing import Any
from src.classes import Product, Category


@pytest.fixture
def prod_1() -> Any:
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


@pytest.fixture
def prod_2() -> Any:
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def category(prod_1: Product, prod_2: Product) -> Any:
    return Category("Смартфоны", "Смартфоны, как средство не только коммуникации, "
                                 "но и получение дополнительных функций для удобства жизни", [prod_1, prod_2])
