import secrets
from flask import session, request


def enable_csrf():
    if session.get("csrf_token") is None:
        session["csrf_token"] = secrets.token_hex(16)


def validate_csrf():
    form_csrf = request.form.get("csrf_token")
    session_csrf = session.get("csrf_token")

    if form_csrf is None or session_csrf is None:
        return False

    return form_csrf == session.get("csrf_token")