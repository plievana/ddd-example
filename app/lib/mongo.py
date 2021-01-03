from flask import Flask
from pymongo import MongoClient


class MongoDB:
    __slots__ = ('_client', '_db')

    def __init__(self):
        self._client = None
        self._db = None

    def init_app(self, app: Flask):
        self._client = MongoClient(app.config['MONGO_HOST'], app.config['MONGO_PORT'], connect=False)
        self._db = self._client[app.config['MONGO_DB']]

    def __getitem__(self, item):
        if not self._client or not self._db:
            raise Exception("Connection must be initiated with init_app")
        return self._db[item]

    def __getattr__(self, item):
        if not self._client or not self._db:
            raise Exception("Connection must be initiated with init_app")
        return self._db[item]
