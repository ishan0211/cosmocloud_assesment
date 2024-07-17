from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints.products import router as product_router
from app.api.endpoints.orders import router as order_router
from app.api.endpoints.users import router as user_router
from app.core.database import get_db
from app.core import config

APP_ENV = config.APP_ENV

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await get_db()
    return


@app.get("/service/health")
async def health():
    return {"status": "ok"}


app.include_router(router=product_router, prefix="/service")
app.include_router(router=order_router, prefix="/service")
app.include_router(router=user_router, prefix="/service")