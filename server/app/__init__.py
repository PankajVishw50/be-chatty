from flask import Flask


def create_app():
    app = Flask(__name__)
    app.secret_key = "Very secret"

    return app


