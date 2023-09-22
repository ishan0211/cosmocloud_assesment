from pydantic import BaseModel

class CreateOrderRequest(BaseModel):
    city: str
    country: str
    zip_code: str