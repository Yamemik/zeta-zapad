from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.common.settings import settings

from src.routes.settings_route import settings_router
from src.routes.auth_route import auth_router
from src.routes.users_route import users_router
from src.routes.carts_route import carts_router
from src.routes.roles_route import roles_router
from src.routes.orders_route import orders_router


def create_app():
    app = FastAPI(
        debug=settings.debug,
        docs_url="/api/docs",
        title=f"{settings.app_name} API docs",
    )

    origins = [
        "http://localhost.tiangolo.com",
        "https://localhost.tiangolo.com",
        "http://localhost:8000",
        "http://localhost:8080",
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(settings_router)
    app.include_router(auth_router)
    app.include_router(users_router)
    app.include_router(carts_router)
    app.include_router(roles_router)
    app.include_router(orders_router)

    return app
