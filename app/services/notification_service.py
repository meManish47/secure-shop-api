from app.utils.email import EmailSender
import pickle
import base64

class NotificationService:
    def __init__(self):
        self.mailer = EmailSender()
        
    def send_receipt(self, user_id, amount):
        body = f"Your payment of {amount} was successful."
        self.mailer.send(user_id, "Payment Receipt", body)
        
    def process_bounced_events(self, payload_b64):
        # Vulnerability: pickle.loads() on untrusted data
        try:
            raw_data = base64.b64decode(payload_b64)
            events = pickle.loads(raw_data)
            for event in events:
                print(f"Processed bounce for {event}")
        except Exception:
            pass