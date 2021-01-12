from flask import Flask
from dependency_injector import load_dependencies


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    load_dependencies(app)

    from apps.api import bp as api_bp
    app.register_blueprint(api_bp)

    return app
