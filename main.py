from threading import Thread

import uvicorn

from alarm_server.server import Server
from consts import SERVER_PORT, SERVER_HOST
from notifier.notifier import Notifier


def run_server():
    uvicorn.run(app=Server().app, host=SERVER_HOST, port=SERVER_PORT)


def run_notifier():
    Notifier().start()


if __name__ == '__main__':
    server = Thread(target=run_server)
    notifier = Thread(target=run_notifier)
    server.start()
    notifier.start()
    for thread in [server, notifier]:
        thread.join()
