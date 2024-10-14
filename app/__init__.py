from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        from . import routes  # Import routes here
        routes.init_routes(app)  # Initialize routes with the app instance
        db.create_all()  # Create database tables if needed

    return app
