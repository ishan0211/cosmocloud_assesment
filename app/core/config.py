import os

APP_ENV = os.environ.get("APP_ENV", "development")
APP_NAME = os.environ.get("APP_NAME", "cosmocloud-assesment")
MONGO_URI = os.environ.get(
    "MONGODB_URL",
    f"mongodb://root:root@localhost:27017/?authMechanism=DEFAULT&appname={APP_NAME}",
)
MONGO_DB = os.environ.get("MONGO_DB", "test")