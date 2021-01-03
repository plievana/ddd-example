from flask import Flask
from app.lib.mongo import MongoDB
db = MongoDB()


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile("config.py")
    
    # Database
    db.init_app(app)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp)

    return app