import os

class Config:
    SECRET_KEY = "FLKWEJFOWIEJFOWKLJFWEOJFOOWEIKFJJOEWIFJOOEWI"

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("local-chatapp-database-link")


class TestingConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = os.environ.get("chatapp-secret-key")
    SQLALCHEMY_DATABASE_URI = os.environ.get("chatapp-database-link")


config = {
    "default": DevelopmentConfig,
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}
