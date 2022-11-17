from functools import lru_cache
import databases

from settings import app_config


@lru_cache()
def get_settings():
    return app_config.Settings()


settings = get_settings()

conn = databases.Database(settings.DATABASE_URL)
