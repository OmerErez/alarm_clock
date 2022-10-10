import time
from threading import Thread
from alarm_server.server import Server
import uvicorn

from notifier.notifier import Notifier


def run_server():
    server = Server()
    uvicorn.run(app=server.app, host='127.0.0.1', port=80)


def run_notifier():
    Notifier().start()


if __name__ == '__main__':
    Thread(target=run_server).start()
    Thread(target=run_notifier).start()
    while True:
        time.sleep(1)
