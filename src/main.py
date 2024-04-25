from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.common.settings import settings
from src.routes.auth_route import auth_router
from src.routes.users_route import users_router
from src.routes.carts_route import carts_router


def create_app():
    app = FastAPI(
        debug=settings.debug,
        docs_url="/api/docs",
        title=f"{settings.app_name} API docs",
    )

    origins = [
        "http://localhost.tiangolo.com",
        "https://localhost.tiangolo.com",
        "http://localhost",
        "http://localhost:8080",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(auth_router)
    app.include_router(users_router)
    app.include_router(carts_router)

    return app



