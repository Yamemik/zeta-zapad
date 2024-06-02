from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # common
    app_name: str = "Zeta-Zapad"
    debug: bool = True
    # owner
    email: str = "kuancarlos@yandex.ru"
    telephone: str = "kuancarlos@yandex.ru"


settings = Settings()
