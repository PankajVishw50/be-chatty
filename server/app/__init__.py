from flask import Flask

from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()


def create_app(config_name="default"):
    app = Flask(__name__)
    app.secret_key = "Very secret"

    app.config.from_object(config[config_name])

    db.init_app(app)

    from .main import main as main_blueprint
    from .avatar import avatar as avatar_blueprint
    from .auth import auth as auth_blueprint

    app.register_blueprint(avatar_blueprint)
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    return app

