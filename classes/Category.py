from classes.Product import Product


class Category:
    """содержит описание категории"""

    name: str
    description: str
    __products: list
    all_category: int
    all_product: int

    all_category = 0
    all_product = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.__products = products

        Category.all_category += 1
        Category.all_product += len(products)

    @property
    def products(self) -> str:
        count = ""
        for i in self.__products:
            count += f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт. "
        return count

    def add_product(self, product: Product) -> None:
        self.__products.append(product)
        Category.all_product += 1
