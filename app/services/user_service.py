from app.repositories.user_repository import UserRepository

class UserService:
    def __init__(self):
        self.repo = UserRepository()
        
    def get_user_profile(self, user_id):
        return self.repo.find_by_id(user_id)
        
    def save_user(self, user):
        self.repo.save(user)