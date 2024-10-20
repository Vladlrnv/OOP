from src.Category import Category
from src.Products import Product


def test_categories(category: Category) -> None:
    assert category.name == "Смартфоны"
    assert category.description == ("Смартфоны, как средство не только коммуникации, "
                                    "но и получение дополнительных функций для удобства жизни")
    assert Category.product_count == 2
    assert Category.category_count == 1


def test_products(category: Category, prod_3: Product) -> None:
    category.add_product(prod_3)
    assert category.name == "Смартфоны"
    assert category.description == ("Смартфоны, как средство не только коммуникации, "
                                    "но и получение дополнительных функций для удобства жизни")
    assert Category.product_count == 5
    assert Category.category_count == 2
    assert category.products == ("Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\nIphone 15, 210000.0 руб. "
                                 "Остаток: 8 шт.\nIphone 16, 250000.0 руб. Остаток: 2 шт.\n")


def test_str_category(category: Category) -> None:
    assert str(category) == "Смартфоны, количество продуктов: 13 шт.\n"


