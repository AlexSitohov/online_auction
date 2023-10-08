import logging
import os
from sqlalchemy.ext.asyncio import AsyncEngine
from fastapi import FastAPI

from app.api.v1.lot import lot_router
from app.daos.providers import provide_auction_dao
from app.db.connection import provide_session
from app.repositories.providers import (
    provide_auction_repository,
    provide_auction_repository_stub,
)


class Application:
    def __init__(self, engine: AsyncEngine):
        self.app = self._setup_app()
        self.engine: AsyncEngine = engine

    @staticmethod
    def _setup_app() -> FastAPI:
        return FastAPI(
            title="Auction API",
            docs_url="/auction/api/v1/docs",
            redoc_url="/auction/api/v1/redoc",
            openapi_url="/auction/api/v1/openapi.json",
            debug=os.environ.get("DEBUG", True),
        )

    def _setup_sessions(self, engine: AsyncEngine):
        self.session = provide_session(engine)

    def _create_daos(self):
        self.auction_dao = provide_auction_dao(self.session)

    def _create_repositories(self):
        self.auction_repository = lambda: provide_auction_repository(self.auction_dao)

    def _override_dependencies(self):
        self.app.dependency_overrides[
            provide_auction_repository_stub
        ] = self.auction_repository

    def _add_routes(self):
        self.app.include_router(lot_router)

    @staticmethod
    def _configure_logging():
        FORMAT = "%(levelname)s %(asctime)s %(filename)s:%(lineno)d %(message)s"
        LEVEL = int(os.environ["LOGGING_LEVEL"])
        logging.basicConfig(level=LEVEL, format=FORMAT)

    def build_application(self):
        self._setup_sessions(self.engine)
        self._create_daos()
        self._create_repositories()
        self._override_dependencies()
        self._add_routes()
        self._configure_logging()

        return self
