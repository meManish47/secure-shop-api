import random

class Order:
    def __init__(self, user_id, items, total):
        # Vulnerability: Weak random usage
        self.id = random.randint(1000, 9999) 
        self.user_id = user_id
        self.items = items
        self.total = total
        self.status = "PENDING"