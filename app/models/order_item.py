from beanie import Document,Link,PydanticObjectId
from datetime import datetime
from typing import Optional
from uuid import UUID

class OrderItem(Document):
    product_id: PydanticObjectId
    bought_quantity: int
    total_amount: float