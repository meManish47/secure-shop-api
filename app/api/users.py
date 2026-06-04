from app.services.user_service import UserService

def get_user(user_id: int):
    user_service = UserService()
    return user_service.get_user_profile(user_id)

# AI Review Target: duplicated logic
def update_user_email(user_id: int, new_email: str):
    user_service = UserService()
    user = user_service.get_user_profile(user_id)
    if not user:
        return {"error": "not found"}
    user.email = new_email
    user_service.save_user(user)
    return {"status": "updated"}

def update_user_address(user_id: int, new_address: str):
    user_service = UserService()
    user = user_service.get_user_profile(user_id)
    if not user:
        return {"error": "not found"}
    user.address = new_address
    user_service.save_user(user)
    return {"status": "updated"}