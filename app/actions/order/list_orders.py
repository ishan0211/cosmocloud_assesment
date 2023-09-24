from app.exceptions.service_exception import ServiceException
from app.models.order import Order
from app.constants.service_constants import Status


class ListOrders:
    def __init__(self,page: int = 1, page_limit: int = 10):
        self.page = page
        self.page_limit = page_limit

    async def run(self):
        try:
            query = {}
            query["status"] = Status.ACTIVE.value
            offset = (self.page - 1) * self.page_limit
            all_orders = await Order.find(query).skip(offset).limit(self.page_limit).to_list()
            return all_orders
        except ServiceException as e:
            raise ServiceException(str(e))
        