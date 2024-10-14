from src.classes import Product, Category


def test_product(prod_1: Product, prod_2: Product) -> None:
    assert prod_1.name == "Samsung Galaxy C23 Ultra"
    assert prod_1.description == "256GB, Серый цвет, 200MP камера"
    assert prod_1.price == 180000.0
    assert prod_1.quantity == 5
    assert prod_2.name == "Iphone 15"
    assert prod_2.description == "512GB, Gray space"
    assert prod_2.price == 210000.0
    assert prod_2.quantity == 8


def test_categories(category: Category) -> None:
    assert category.name == "Смартфоны"
    assert category.description == ("Смартфоны, как средство не только коммуникации, "
                                    "но и получение дополнительных функций для удобства жизни")
    assert len(category.product) == 2
    assert Category.category_count == 1
