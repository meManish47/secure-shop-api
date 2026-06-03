from app.repositories.user_repository import UserRepository
from app.security.jwt_handler import JWTHandler
from app.utils.hashing import verify_password

class AuthService:
    def __init__(self):
        self.user_repo = UserRepository()
        self.jwt_handler = JWTHandler()

    def authenticate(self, username, password):
        user = self.user_repo.find_by_username(username)
        if user and verify_password(password, user.password_hash):
            return self.jwt_handler.generate_token(user.id)
        return None\n