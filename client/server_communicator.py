from requests import get, post, put, delete


class ServerCommunicator:
    def __init__(self, server_base_url: str):
        self.server_base_url = server_base_url

    def get(self, path: str):
        return get(f'{self.server_base_url}/{path}')

    def post(self, path: str, json: dict):
        return post(f'{self.server_base_url}/{path}', json=json)

    def put(self, path: str, json: dict):
        return put(f'{self.server_base_url}/{path}', json=json)

    def delete(self, path: str):
        return delete(f'{self.server_base_url}/{path}')
