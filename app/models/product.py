from beanie import Document
from typing import Optional

class Product(Document):
    product_name: str
    product_price: float
    product_available_quantity: Optional[int] = 0