from beanie import Link
from pydantic import BaseModel
from app.models.product import Product

class OrderItem(BaseModel):
    product_id: Link[Product]
    bought_quantity: int