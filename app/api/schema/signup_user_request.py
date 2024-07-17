from pydantic import BaseModel
from typing import Optional

class CreateSignupRequest(BaseModel):
    name: str
    password: str
    email: str
    user_type: str