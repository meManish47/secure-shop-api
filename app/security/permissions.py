# AST requirement: Decorator
def require_auth(func):
    def wrapper(*args, **kwargs):
        # Mock auth check
        print("Checking auth...")
        return func(*args, **kwargs)
    return wrapper\n