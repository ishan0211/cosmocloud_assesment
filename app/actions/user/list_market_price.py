from app.exceptions.service_exception import ServiceException
from app.models.marketprice import MarketPrice
from app.constants.service_constants import Status

class ListMarketPrice:
    def __init__(self,name: str,page: int = 1, page_limit: int = 20):
        self.name = name
        self.page = page
        self.page_limit = page_limit

    async def run(self):
        try:
            query = {}
            if self.name:
                query["name"] = self.name
            offset = (self.page - 1) * self.page_limit
            all_orders = await MarketPrice.find(query).skip(offset).limit(self.page_limit).to_list()
            return all_orders
        except ServiceException as e:
            raise ServiceException(str(e))
        