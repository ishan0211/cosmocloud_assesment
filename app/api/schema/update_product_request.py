from pydantic import BaseModel
from typing import Optional

class UpdateProductRequest(BaseModel):
    product_name: str
    product_price: Optional[float] = None
    product_available_quantity: Optional[int] = None