
import jwt
import datetime
from typing import Optional, Dict, Any

class AuthManager:
    def __init__(self):
        self.secret_key = "your-secret-key-change-this"
        self.users = {
            "admin": {"password": "password123", "role": "admin"},
            "viewer": {"password": "viewerpass", "role": "viewer"}
        }

    def authenticate(self, username: str, password: str) -> Optional[str]:
        if username in self.users and self.users[username]["password"] == password:
            payload = {
                "username": username,
                "role": self.users[username]["role"],
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }
            return jwt.encode(payload, self.secret_key, algorithm="HS256")
        return None

    def verify_token(self, token: str) -> Dict[str, Any]:
        try:
            return jwt.decode(token, self.secret_key, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return {"error": "Token expired"}
        except jwt.InvalidTokenError:
            return {"error": "Invalid token"}

    def require_role(self, required_role: str):
        def decorator(f):
            def wrapper(*args, **kwargs):
                token = kwargs.get('token')
                if not token:
                    return {"error": "No token provided"}, 401
                payload = self.verify_token(token)
                if "error" in payload:
                    return {"error": payload["error"]}, 401
                if payload["role"] != required_role:
                    return {"error": "Insufficient permissions"}, 403
                return f(*args, **kwargs)
            return wrapper
        return decorator
