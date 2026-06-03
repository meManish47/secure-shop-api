from app.repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self):
        self.repo = ProductRepository()
        
    def search(self, query, filters):
        # some dummy implementation
        products = self.repo.get_all()
        return [p for p in products if query.lower() in p.name.lower()]\n