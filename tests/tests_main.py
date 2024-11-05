import unittest
from src.main import Product, Category, Smartphone, LawnGrass


class TestProduct(unittest.TestCase):

    def test_product_creation(self):
        product = Product("Test Product", "Description", 10.0, 5)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.description, "Description")
        self.assertEqual(product.price, 10.0)
        self.assertEqual(product.quantity, 5)

    def test_product_creation_with_zero_quantity(self):
        with self.assertRaises(ValueError):
            Product("Invalid Product", "Description", 10.0, 0)

    def test_product_price_setter(self):
        product = Product("Test Product", "Description", 10.0, 5)
        product.price = 15.0
        self.assertEqual(product.price, 15.0)

    def test_product_price_setter_with_invalid_value(self):
        product = Product("Test Product", "Description", 10.0, 5)
        product.price = -5.0
        self.assertEqual(product.price, 10.0)

    def test_product_new_product(self):
        product_info = {"name": "Test Product", "description": "Description", "price": 10.0, "quantity": 5}
        product = Product.new_product(product_info)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.description, "Description")
        self.assertEqual(product.price, 10.0)
        self.assertEqual(product.quantity, 5)

    def test_product_add(self):
        product1 = Product("Product 1", "Description 1", 10.0, 2)
        product2 = Product("Product 2", "Description 2", 20.0, 3)
        total_price = product1.add(product2)
        self.assertEqual(total_price, 80.0)  # (10 * 2) + (20 * 3)

    def test_product_add_with_invalid_type(self):
        product1 = Product("Product 1", "Description 1", 10.0, 2)
        with self.assertRaises(TypeError):
            product1.add("Invalid Object")


class TestSmartphone(unittest.TestCase):

    def test_smartphone_creation(self):
        smartphone = Smartphone("Test Smartphone", "Description", 500.0, 3, 90.0, "Model X", 128, "Black")
        self.assertEqual(smartphone.efficiency, 90.0)
        self.assertEqual(smartphone.model, "Model X")
        self.assertEqual(smartphone.memory, 128)
        self.assertEqual(smartphone.color, "Black")


class TestLawnGrass(unittest.TestCase):

    def test_lawn_grass_creation(self):
        lawn_grass = LawnGrass("Test Lawn Grass", "Description", 15.0, 10, "USA", "3-5 weeks", "Green")
        self.assertEqual(lawn_grass.country, "USA")
        self.assertEqual(lawn_grass.germination_period, "3-5 weeks")
        self.assertEqual(lawn_grass.color, "Green")


class TestCategory(unittest.TestCase):

    def test_category_creation(self):
        products = [Product("Product 1", "Description 1", 10.0, 2), Product("Product 2", "Description 2", 20.0, 3)]
        category = Category("Test Category", "Description", products)
        self.assertEqual(category.name, "Test Category")
        self.assertEqual(category.description, "Description")
        self.assertEqual(len(category.products), 2)

    def test_category_add_product(self):
        category = Category("Test Category", "Description")
        product = Product("New Product", "Description", 30.0, 4)
        category.add_product(product)
        self.assertEqual(len(category.products), 1)

    def test_category_add_invalid_product(self):
        category = Category("Test Category", "Description")
        with self.assertRaises(TypeError):
            category.add_product("Invalid Product")


if __name__ == "__main__":
    unittest.main()
