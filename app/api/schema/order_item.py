from beanie import PydanticObjectId
from pydantic import BaseModel

class OrderItem(BaseModel):
    product_id: PydanticObjectId
    bought_quantity: int