from _pytest import warnings


class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        """Возвращает цену, обрабатывая валидацию."""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Проверяет цену перед установкой."""
        if new_price <= 0:
            warnings.warn("Цена не должна быть нулевая или отрицательная", UserWarning)
        else:
            self.__price = new_price

    @classmethod
    def from_dict(cls, product_data):
        """Создает объект Product из словаря."""
        return cls(
            product_data["name"],
            product_data["description"],
            product_data["price"],
            product_data["quantity"],
        )

    def __str__(self):
        """Представляет продукт в виде строки."""
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Складывает стоимость продуктов."""
        if isinstance(other, Product):
            return (self.price * self.quantity) + (other.price * other.quantity)
        return NotImplemented


class Category:
    _total_categories = 0
    _total_products = 0

    def __init__(self, name, description, products=None):
        if products is None:
            products = []
        self.name = name
        self.description = description
        self._products = products
        self._update_counts()

    def _update_counts(self):
        """Обновляет счетчики категорий и продуктов."""
        Category._total_categories += 1
        Category._total_products += len(self._products)

    @staticmethod
    def get_total_categories():
        """Возвращает общее количество категорий."""
        return Category._total_categories

    @staticmethod
    def get_total_products():
        """Возвращает общее количество продуктов."""
        return Category._total_products

    def add_product(self, product):
        """Добавляет продукт в категорию."""
        self._products.append(product)
        Category._total_products += 1

    @property
    def products(self):
        """Возвращает строку с описанием всех продуктов в категории."""
        return "\n".join(str(product) for product in self._products)

    def __str__(self):
        """Представляет категорию в виде строки."""
        return f"{self.name}, количество продуктов: {Category._total_products} шт."

    def __add__(self, other):
        """Складывает общую стоимость продуктов в категориях."""
        if not isinstance(other, Category):
            raise TypeError("Can only add Category objects")
        total_value = 0
        for product in self._products:
            total_value += product.price * product.quantity
        for product in other._products:
            total_value += product.price * product.quantity
        return total_value


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 3)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1)
    print(product2)
    print(product3)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3]
    )

    print(category1)
    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)
