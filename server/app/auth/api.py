from . import auth
from flask import request

from .utils import is_account_available


@auth.post("/api/available")
def check_availability():
    username = request.form.get("username")
    tag = request.form.get("tag")

    try:
        tag = int(tag)

        if 1000 > tag or tag > 9999:
            raise ValueError("Invalid value")
    except Exception as e:
        return {
            "error": "only accepts integer value between 1000 <= value <= 9999"
        }, 400

    if not username or not tag or not isinstance(tag, int):
        return {
            "error": "Provide valid field data"
        }, 400

    data = is_account_available(username, tag)

    if data:
        return {
            "available": False,
            "error": None
        }

    return {
        "available": True,
        "error": None
    }