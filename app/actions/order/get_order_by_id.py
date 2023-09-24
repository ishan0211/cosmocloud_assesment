from beanie import PydanticObjectId
from app.models.order import Order

class GetOrderById():
    def __init__(self,order_id: PydanticObjectId):
        self.order_id = order_id
    
    async def run(self):
        order = await Order.get(self.order_id)
        return order