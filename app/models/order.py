from beanie import Document
from typing import List
from datetime import datetime
from app.api.schema.order_item import OrderItem
from app.api.schema.user_address import UserAddress

class Order(Document):
    items: List[OrderItem]
    user_address: UserAddress
    timestamp: datetime