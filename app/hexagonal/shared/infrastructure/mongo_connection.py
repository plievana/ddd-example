from pymongo import MongoClient

from app.hexagonal.shared.infrastructure.db_connection import DBConnection


class MongoDB(DBConnection):
    __slots__ = ('client', 'db')

    def __init__(self, host, port, db, user, password):
        self.client = MongoClient(host, port, connect=False)
        self.db = self.client[db]
