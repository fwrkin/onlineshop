from abc import ABC, abstractmethod


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity

    @property
    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class LoggerMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"Создан объект класса {self.__class__.__name__} с параметрами: {args}")


class Product(LoggerMixin, BaseProduct):
    product_count = 0

    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        Product.product_count += 1

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self._price = new_price
        else:
            raise ValueError("Цена должна быть положительной")

    def __str__(self):
        return f"{self.name}: {self.price:.2f} руб. Остаток: {self.quantity} шт."

    def total_value(self):
        return self.price * self.quantity


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        return (
            super().__str__() +
            f", Эффективность: {self.efficiency}, Модель: {self.model}, "
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
            super().__str__() +
            f", Страна: {self.country}, Период прорастания: {self.germination_period}, Цвет: {self.color}"
        )


class ProductCategory:
    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []

    def add_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)
        else:
            raise TypeError("Только продукты могут быть добавлены")

    @property
    def total_product_count(self):
        return sum(product.quantity for product in self.products)

    def __str__(self):
        return f"{self.name}: {self.total_product_count} продуктов"


if __name__ == '__main__':
    # Создание экземпляров смартфонов
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )
    smartphone2 = Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space"
    )
    smartphone3 = Smartphone(
        "Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14, 90.0, "Redmi Note 11", 1024, "Синий"
    )

    # Печать информации о продуктах
    print("\nИнформация о продуктах:")
    for item in (smartphone1, smartphone2, smartphone3):
        print(item)

    # Создание категории продуктов
    category1 = ProductCategory(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и "
        "получения дополнительных функций для удобства жизни",
        [smartphone1, smartphone2, smartphone3]
    )

    # Печать информации о категории
    print("\nИнформация о категории:")
    print(f"Категория: {category1.name}")
    print(f"Описание: {category1.description}")
    print(f"Количество продуктов: {len(category1.products)}")
    print(f"Общее количество товаров: {category1.total_product_count}")

    # Создание другого продукта и добавление его в другую категорию
    product4 = Product(
        "55\" QLED 4K", "Фоновая подсветка", 123000.0, 7
    )
    category2 = ProductCategory(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником",
        [product4]
    )

    print(f"\nИнформация о категории: {category2.name}")
    print(f"Описание: {category2.description}")
    print(f"Количество продуктов: {len(category2.products)}")
    print(f"Общее количество товаров: {category2.total_product_count}")
