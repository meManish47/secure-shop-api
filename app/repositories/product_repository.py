from app.models.product import Product

class ProductRepository:
    def get_all(self):
        return [
            Product(1, "Laptop", 999.99),
            Product(2, "Mouse", 19.99)
        ]