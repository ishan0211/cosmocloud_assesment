from beanie import PydanticObjectId
from pydantic import BaseModel
from typing import List
from app.api.schema.order_item import OrderItem
from app.api.schema.user_address import UserAddress

class CreateOrderRequest(BaseModel):
    items: List[OrderItem]
    user_address: UserAddress