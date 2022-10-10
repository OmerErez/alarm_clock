from fastapi import FastAPI

from alarm_server.routing.routes import Routes


class Server:
    def __init__(self):
        self.app = FastAPI()
        self._initialize_app()

    def _initialize_app(self):
        for router in Routes.ROUTERS:
            self.app.include_router(router.fast_api_router, prefix=router.prefix)
