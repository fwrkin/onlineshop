class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price: float):
        if new_price <= 0:
            raise ValueError("Цена должна быть положительной.")
        self._price = new_price

    def __add__(self, other):
        if type(self) is type(other):
            return self.quantity + other.quantity
        raise TypeError("Нельзя складывать продукты разных категорий.")

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return (
            super().__str__() + f", Эффективность: {self.efficiency}, Модель: {self.model}, "
            f"Память: {self.memory}, Цвет: {self.color}"
        )


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        return (
            super().__str__() + f", Страна: {self.country}, Срок прорастания: {self.germination_period}, "
            f"Цвет: {self.color}"
        )


class Category:
    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только продукты или их подклассы.")
        self.products.append(product)

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self.products)} шт."


if __name__ == "__main__":
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15 Pro Max", 512, "Gray space")
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.3, "Note 11", 1024, "Синий")

    grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")

    smartphone_sum = smartphone1 + smartphone2
    print(f"Общее количество смартфонов: {smartphone_sum}")

    grass_sum = grass1 + grass2
    print(f"Общее количество газонов: {grass_sum}")

    try:
        invalid_sum = smartphone1 + grass1
    except TypeError as e:
        print("Возникла ошибка TypeError при попытке сложения:", e)

    category_smartphones = Category("Смартфоны", "Высокотехнологичные смартфоны", [smartphone1, smartphone2])
    category_grass = Category("Газонная трава", "Различные виды газонной травы", [grass1, grass2])

    category_smartphones.add_product(smartphone3)
    print([product.name for product in category_smartphones.products])

    try:
        category_smartphones.add_product("Not a product")
    except TypeError as e:
        print("Возникла ошибка TypeError при добавлении не продукта:", e)
