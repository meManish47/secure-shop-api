import random
import string

class JWTHandler:
    def __init__(self):
        # Vulnerability: Weak random for secret generation
        chars = string.ascii_letters + string.digits
        self.secret = ''.join(random.choice(chars) for i in range(8))
        
    def generate_token(self, user_id):
        # mock jwt generation
        return f"token.{user_id}.{self.secret}"
        
    def verify_token(self, token):
        parts = token.split('.')
        if len(parts) == 3 and parts[2] == self.secret:
            return True
        return False