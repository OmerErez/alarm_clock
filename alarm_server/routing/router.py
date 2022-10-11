from typing import List

from fastapi.routing import APIRoute, APIRouter


class Router:
    def __init__(self, prefix: str, routes: List[APIRoute]):
        self.prefix = prefix
        self.routes = routes

    @property
    def fast_api_router(self):
        return APIRouter(prefix=self.prefix, routes=self.routes)
