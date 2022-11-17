from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "PYTHON!!!"
    DATABASE_URL: str

    class Config:
        env_file = ".env"


settings = Settings()
