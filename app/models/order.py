from beanie import Document
from app.models.order_item import OrderItem
from app.models.user_address import UserAddress
from typing import List

class Order(Document):
    timestamp: str 
    items: List[OrderItem]
    user_address: UserAddress