class Category:
    """содержит описание категории"""

    name: str
    description: str
    products: list
    all_category: int
    all_product: int

    all_category = 0
    all_product = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products

        Category.all_category += 1
        Category.all_product += len(products)
