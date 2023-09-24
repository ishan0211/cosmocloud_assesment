from app.exceptions.service_exception import ServiceException
from typing import List
from app.constants.service_constants import Status
from app.api.schema.create_order_request import OrderItem,UserAddress
from app.models.order import Order
from datetime import datetime
from app.models.product import Product
from beanie.operators import In
from beanie import PydanticObjectId
from fastapi import HTTPException

class CreateOrder:
    def __init__(self,items: List[OrderItem],user_address: UserAddress):
        self.items = items
        self.user_address = user_address
    
    def find_order_item(self,id: PydanticObjectId):
        for item in self.items:
            if(item.product_id == id):
                return item.bought_quantity
        return -1

    async def deduct_product_count_for_order(self):
        product_ids = [order_item.product_id for order_item in self.items]
        products = await Product.find(In(Product.id,product_ids)).to_list()

        if (len(products)!=len(product_ids)):
            raise HTTPException(status_code=404,detail="one of the product is not present")
        for product in products:
            bought_quantity = self.find_order_item(product.id)
            if bought_quantity>product.product_available_quantity:
                raise HTTPException(status_code=404,detail="quantity bought exceeds available quantity")
            product.product_available_quantity = product.product_available_quantity - bought_quantity
            await product.save()
        return products

    async def run(self):
        try:
            products = await self.deduct_product_count_for_order()
            print(products)
            create_order_request = {
                "items": self.items,
                "user_address": self.user_address,
                "status": Status.ACTIVE.value,
                "created_at": datetime.now(),
                "updated_at": datetime.now()
            }
            print(create_order_request)
            new_order = Order(**dict(create_order_request))
            await new_order.create()
            return dict(new_order)["id"]
        except ServiceException as e:
            raise ServiceException(str(e))
        