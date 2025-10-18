# app/__init__.py
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "main.login"

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    # Basic config (override SECRET_KEY in production via env var)
    app.config.from_mapping(
        SECRET_KEY = os.environ.get("SECRET_KEY", "dev-key-change-this"),
        SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL",
                                                "sqlite:///" + os.path.join(app.instance_path, "app.sqlite")),
        SQLALCHEMY_TRACK_MODIFICATIONS = False,
    )

    if test_config:
        app.config.update(test_config)

    # ensure instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    db.init_app(app)
    login_manager.init_app(app)

    # Import models and create tables
    from . import models
    with app.app_context():
        db.create_all()

    # Register routes
    from .routes import bp
    app.register_blueprint(bp)

    # Mount dashboard
    from .dashboard import create_dashboard
    create_dashboard(app)

    # User loader for Flask-Login
    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        try:
            return User.query.get(int(user_id))
        except Exception:
            return None

    return app
