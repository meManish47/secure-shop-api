from app.database.connection import get_db
from app.models.user import User

class UserRepository:
    def find_by_id(self, user_id):
        db = get_db()
        # Mocking db fetch
        return User(user_id, "testuser", "dummyhash")
        
    def find_by_username(self, username):
        return User(1, username, "dummyhash")
        
    def save(self, user):
        pass\n