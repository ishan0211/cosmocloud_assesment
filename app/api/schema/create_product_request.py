from pydantic import BaseModel
from typing import Optional

class CreateProductRequest(BaseModel):
    product_name: str
    product_price: float
    product_available_quantity: Optional[int] = 0