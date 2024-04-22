from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # common
    app_name: str = "Zeta-Zapad"
    debug: bool = True


settings = Settings()
