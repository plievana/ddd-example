from flask import Blueprint
from flask_restful import Api

from src.hexagonal.status.infrastructure.dependency_injection import StatusModuleDependencyContainer


bp = Blueprint('api', __name__)
api = Api(bp)

status_dependencies = StatusModuleDependencyContainer()


from .routes import register_routes
register_routes(api)

