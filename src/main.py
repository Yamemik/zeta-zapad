from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from src.common.settings import settings


def create_app():
    app = FastAPI(
        debug=settings.debug,
        docs_url="/api/docs",
        title="Moto-BRO API docs",
    )

    return app
