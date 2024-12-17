import jwt
import datetime

SECRET_KEY = "your-secret-key"

class AuthManager:
    def __init__(self):
        self.users = {"admin": "password123", "viewer": "viewerpass"}

    def authenticate(self, username, password):
        if username in self.users and self.users[username] == password:
            payload = {
                "username": username,
                "role": "admin" if username == "admin" else "viewer",
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
            }
            return jwt.encode(payload, SECRET_KEY, algorithm="HS256")
        return None

    @staticmethod
    def verify_token(token):
        try:
            return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            return "Token expired."
        except jwt.InvalidTokenError:
            return "Invalid token."
