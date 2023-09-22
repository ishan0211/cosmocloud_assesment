from pydantic import BaseModel

class UserSessionResponse(BaseModel):
    message: str
    data: dict
    status: int
