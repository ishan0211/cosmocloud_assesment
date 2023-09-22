from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from app.core import config
from app.models import __all_models__


async def get_db():
    client = AsyncIOMotorClient(config.MONGO_URI)
    await init_beanie(database=client[config.MONGO_DB], document_models=__all_models__)
