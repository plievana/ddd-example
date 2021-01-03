import os

MONGO_HOST = os.environ.get('MONGO_HOST') or 'localhost'
MONGO_PORT = os.environ.get('MONGO_PORT') or 27017
MONGO_DB = os.environ.get('MONGO_DB') or 'ddd'
