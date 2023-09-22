from pydantic import BaseModel

class SessionResponse(BaseModel):
    message: str
    data: dict
    status: int
