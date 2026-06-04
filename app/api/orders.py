from app.services.order_service import OrderService
from app.security.permissions import require_auth

@require_auth
def create_order(user_id: int, items: list):
    service = OrderService()
    return service.place_order(user_id, items)

@require_auth
def get_order_status(user_id: int, order_id: str):
    service = OrderService()
    return service.get_status(order_id)