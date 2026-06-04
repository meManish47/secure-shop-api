from app.services.payment_service import PaymentService

def process_webhook(payload: dict):
    # Insecure coding pattern: no signature validation
    service = PaymentService()
    if payload.get("status") == "success":
        service.confirm_payment(payload.get("transaction_id"))
    return {"status": "ok"}