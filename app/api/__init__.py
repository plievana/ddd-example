from flask import Blueprint
from flask_restful import Api

bp = Blueprint('api', __name__)
api = Api(bp)

from .endpoints import register_endpoints
register_endpoints(api)
