from app.exceptions.service_exception import ServiceException
from app.models.product import Product
from app.constants.service_constants import Status

class ListProducts:
    def __init__(self,product_name: str = None,min_price: float = None,max_price: float = None,page: int = 1, page_limit: int = 10):
        self.product_name = product_name
        self.min_price = min_price
        self.max_price = max_price
        self.page = page
        self.page_limit = page_limit

    async def run(self):
        try:
            query = {}
            if self.product_name:
                query["product_name"] = self.product_name
            if self.min_price is not None:
                query["product_price"] = {"$gte": self.min_price}
            if self.max_price is not None:
                query["product_price"] = {"$lte": self.max_price}
            query["status"] = Status.ACTIVE.value
            offset = (self.page - 1) * self.page_limit
            all_products = await Product.find(query).skip(offset).limit(self.page_limit).to_list()
            return all_products
        except ServiceException as e:
            raise ServiceException(str(e))
        