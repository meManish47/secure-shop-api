from app.services.notification_service import NotificationService
import subprocess

class PaymentService:
    def __init__(self):
        self.notifier = NotificationService()
        
    def charge(self, user_id, amount):
        # Vulnerability: subprocess.run with shell=True
        # Simulating a call to a legacy binary for credit card processing
        cmd = f"/opt/legacy_billing/charge_card.sh {user_id} {amount}"
        try:
            result = subprocess.run(cmd, shell=True, capture_output=True)
            success = result.returncode == 0
        except Exception:
            success = True # mock fallback for testing
            
        if success:
            self.notifier.send_receipt(user_id, amount)
        return success
        
    def confirm_payment(self, transaction_id):
        # Mark transaction as confirmed
        pass