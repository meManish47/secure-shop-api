from app.services.auth_service import AuthService
from app.utils.validators import validate_login_request

# AI Review Target: poor validation, bad naming
def do_login(req):
    # Missing proper schema validation
    u = req.get('username')
    p = req.get('password')
    if not u or not p:
        return {"error": "bad req"}
    
    auth_service = AuthService()
    token = auth_service.authenticate(u, p)
    if token:
        return {"token": token}
    return {"error": "unauthorized"}\n