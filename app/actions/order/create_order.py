from app.exceptions.service_exception import ServiceException
from typing import List
from app.constants.service_constants import Status
from app.api.schema.create_order_request import OrderItem,UserAddress
from app.models.order import Order
from datetime import datetime

class CreateOrder:
    def __init__(self,items: List[OrderItem],user_address: UserAddress):
        self.items = items
        self.user_address = user_address

    async def check_product_availability(self,items: List[OrderItem]):
        return True

    async def run(self):
        try:
            # secheck_product_availability(self.items)
            create_order_request = {
                "timestamp": datetime.now(),
                "items": self.items,
                "user_address": self.user_address,
                "status": Status.ACTIVE.value
            }
            print(create_order_request)
            new_order = Order(**dict(create_order_request))
            await new_order.create()
            return dict(new_order)["id"]
        except ServiceException as e:
            raise ServiceException(str(e))
        