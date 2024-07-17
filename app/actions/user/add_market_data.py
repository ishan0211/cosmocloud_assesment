from app.exceptions.service_exception import ServiceException
from typing import Optional
from app.models.marketprice import MarketPrice
from app.constants.service_constants import Status
from fastapi import HTTPException
from datetime import datetime
import httpx

class AddMarketData:
    def __init__(self):
        pass

    async def run(self):
        try:
            url = f'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin,ethereum,tether,binancecoin,solana&x_cg_api_key=CG-1kvHUtp8NxLwZpBwS1wbwb8s'
            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                data = response.json()
            required_data = {}
            for dat in data:
                create_market_price_request = {
                    "name": dat["name"],
                    "symbol": dat["symbol"],
                    "market_cap_rank": float(dat["market_cap_rank"]),
                    "current_price": float(dat["current_price"]),
                    "created_at": datetime.now(),
                    "updated_at": datetime.now(),
                }
                new_entry = MarketPrice(**dict(create_market_price_request))
                await new_entry.create()
        except ServiceException as e:
            raise ServiceException(str(e))
        