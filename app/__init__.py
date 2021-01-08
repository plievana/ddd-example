from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")

    from app.entry_points.api import create_blueprint as create_api
    app.register_blueprint(create_api(app.config))

    return app
