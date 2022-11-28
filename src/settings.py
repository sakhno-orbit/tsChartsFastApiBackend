import logging
from functools import lru_cache
from pydantic import BaseSettings

logger = logging.getLogger(__name__)


class Settings(BaseSettings):

    MONGODB_USER: str = "root"
    MONGODB_PASSWORD: str = "rootpassword"
    MONGODB_HOST: str = "localhost"
    MONGODB_PORT: str = "27017"


@lru_cache()
def configure_settings():
    return Settings()


settings = configure_settings()
