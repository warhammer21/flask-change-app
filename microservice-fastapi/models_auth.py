from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    username: str
    full_name: Optional[str] = None
    email: Optional[str] = None
    hashed_password: str
    disabled: Optional[bool] = None


class Token(BaseModel):
    access_token: str
    token_type: str


# Simulated "database" with pre-hashed password
fake_users_db = {
    "testuser": {
        "username": "testuser",
        "full_name": "Test User",
        "email": "testuser@example.com",
        "hashed_password": "$2b$12$.vEbzZNXTNXInEr8epig1e5NoaoR/bmbPaymbMnIf/ccE31kZSyfi",  # Hashed for "testpassword"
        "disabled": False,
    }
}
