from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # common
    app_name: str = "Moto-BRO"
    debug: bool = True


settings = Settings()
