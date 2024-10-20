from typing import Any


class Category:
    """ Класс определяющий категории товаров """
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None) -> None:
        """ Функция инициализации """
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def add_product(self, product: Any) -> None:
        """ Функция добавляет новый продукт """
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """ Декоратор для чтения приватного атрибута __products"""
        new_str = ""
        for product in self.__products:
            new_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return new_str

    def __str__(self):
        all_prod = 0
        for num in self.__products:
            all_prod += num.quantity
        return f"{self.name}, количество продуктов: {all_prod} шт.\n"
