from app.repositories.order_repository import OrderRepository
from app.services.payment_service import PaymentService
from app.models.order import Order
import tempfile
import os

class OrderService:
    def __init__(self):
        self.repo = OrderRepository()
        self.payment_service = PaymentService()
        
    def place_order(self, user_id, items):
        total = sum([item['price'] for item in items])
        order = Order(user_id, items, total)
        self.repo.save(order)
        
        # Method call across services
        success = self.payment_service.charge(user_id, total)
        if success:
            order.status = "PAID"
            self.generate_receipt(order)
        else:
            order.status = "FAILED"
            
        self.repo.save(order)
        return order
        
    def get_status(self, order_id):
        order = self.repo.find_by_id(order_id)
        return order.status if order else "NOT_FOUND"
        
    def generate_receipt(self, order):
        # Vulnerability: Insecure temp file usage
        filename = "/tmp/receipt_" + str(order.id) + ".txt"
        with open(filename, "w") as f:
            f.write(f"Receipt for order {order.id} - Total: {order.total}")
        return filename\n