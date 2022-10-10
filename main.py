import time
from threading import Thread
from alarm_server.server import Server
import uvicorn

from consts import SERVER_PORT, SERVER_HOST
from notifier.notifier import Notifier


def run_server():
    server = Server()
    uvicorn.run(app=server.app, host=SERVER_HOST, port=SERVER_PORT)


def run_notifier():
    Notifier().start()


if __name__ == '__main__':
    Thread(target=run_server).start()
    Thread(target=run_notifier).start()
    while True:
        time.sleep(1)
