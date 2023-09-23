from beanie import Document
from typing import Optional
from datetime import datetime

class Product(Document):
    product_name: str
    product_price: float
    product_available_quantity: Optional[int] = 0
    status: str
    created_at: datetime
    updated_at: Optional[datetime] = None