from config import TOKEN


class Settings():

    def __init__(self, token):
        self._token = token

    def get_token(self):
        return self._token


def get_settings():
    return Settings(TOKEN)
