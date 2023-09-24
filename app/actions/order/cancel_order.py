from beanie import PydanticObjectId
from beanie.operators import In
from app.models.product import Product
from fastapi import HTTPException
from app.exceptions.service_exception import ServiceException
from app.constants.service_constants import Status
from app.actions.order.get_order_by_id import GetOrderById
from datetime import datetime
from typing import List
from app.api.schema.order_item import OrderItem

class CancelOrder():
    def __init__(self,order_id: PydanticObjectId):
        self.order_id = order_id

    def find_order_item(self,id: PydanticObjectId,items: OrderItem):
        for item in items:
            if(item.product_id == id):
                return item.bought_quantity
        return -1

    async def add_product_count_for_order(self,items: List[OrderItem]):
        product_ids = [order_item.product_id for order_item in items]
        print(product_ids)
        products = await Product.find(In(Product.id,product_ids)).to_list()
        print(products)
        if (len(products)!=len(product_ids)):
            raise HTTPException(status_code=404,detail="one of the product is not present")
        for product in products:
            bought_quantity = self.find_order_item(product.id,items)
            if bought_quantity>product.product_available_quantity:
                raise HTTPException(status_code=404,detail="quantity bought exceeds available quantity")
            product.product_available_quantity = product.product_available_quantity + bought_quantity
            await product.save()
        return products

    async def run(self):
        try:
            order = await GetOrderById(self.order_id).run()
            order_item = order.items
            await self.add_product_count_for_order(order_item)
            order.updated_at = datetime.now()
            order.status = Status.INACTIVE.value
            return dict(order)["id"]
        except ServiceException as e:
            raise ServiceException(str(e))
