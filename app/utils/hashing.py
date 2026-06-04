import hashlib

def hash_password(password: str) -> str:
    # Vulnerability: Weak MD5 hashing
    return hashlib.md5(password.encode()).hexdigest()
    
def verify_password(password: str, hashed: str) -> bool:
    return hash_password(password) == hashed