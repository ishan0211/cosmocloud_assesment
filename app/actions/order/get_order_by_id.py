from beanie import PydanticObjectId
from app.models.order import Order
from app.exceptions.service_exception import ServiceException
from fastapi import HTTPException

class GetOrderById():
    def __init__(self,order_id: PydanticObjectId):
        self.order_id = order_id
    
    async def run(self):
        try:
            order = await Order.get(self.order_id)
            if not order:
                raise HTTPException(status_code=404, detail="order_id is invalid")
            return order
        except ServiceException as e:
            raise ServiceException(str(e))