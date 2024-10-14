import pytest

from src.main import Category, LawnGrass, Product, Smartphone


@pytest.fixture
def setup_products():
    """Создание объектов продуктов для тестирования."""
    smartphone1 = Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, "High", "S23 Ultra", 256, "Серый"
    )
    smartphone2 = Smartphone(
        "Iphone 15", "512GB, Gray space", 210000.0, 8, "Very High", "15 Pro Max", 512, "Space Gray"
    )
    lawn_grass1 = LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
    return smartphone1, smartphone2, lawn_grass1


def test_product_creation():
    product = Product("Тестер", "Тестовый продукт", 100.0, 10)
    assert product.name == "Тестер"
    assert product.price == 100.0
    assert product.quantity == 10


def test_product_str():
    product = Product("Тестер", "Тестовый продукт", 100.0, 10)
    expected_str = "Тестер, 100.0 руб. Остаток: 10 шт."
    assert str(product) == expected_str


def test_product_str_with_setup(setup_products):
    smartphone1, _, _ = setup_products
    expected_str = (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт., "
        "Эффективность: High, Модель: S23 Ultra, Память: 256, Цвет: Серый"
    )
    assert str(smartphone1) == expected_str


def test_add_products(setup_products):
    smartphone1, smartphone2, _ = setup_products
    total_quantity = smartphone1 + smartphone2
    assert total_quantity == 13  # 5 + 8


def test_add_different_product_types(setup_products):
    smartphone1, _, lawn_grass1 = setup_products
    with pytest.raises(TypeError):
        _ = smartphone1 + lawn_grass1


def test_add_product_to_category(setup_products):
    smartphone1, _, _ = setup_products
    smartphone_category = Category("Смартфоны", "Смартфоны и аксессуары")
    smartphone_category.add_product(smartphone1)
    assert len(smartphone_category.products) == 1


def test_add_invalid_product_to_category():
    smartphone_category = Category("Смартфоны", "Смартфоны и аксессуары")
    with pytest.raises(TypeError):
        smartphone_category.add_product("Не продукт")


def test_category_str(setup_products):
    smartphone1, _, _ = setup_products
    smartphone_category = Category("Смартфоны", "Смартфоны и аксессуары", [smartphone1])
    expected_str = "Смартфоны, количество продуктов: 1 шт."
    assert str(smartphone_category) == expected_str


if __name__ == "__main__":
    pytest.main()
