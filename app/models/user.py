from beanie import Document,Indexed
from datetime import datetime

class User(Document):
    name: str
    password: str
    email: Indexed(str, unique=True)
    user_type: str
    status: str
    created_at: datetime
    updated_at: datetime
