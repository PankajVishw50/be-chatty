from . import auth

from flask import render_template
from flask import session
from flask import redirect
from flask import url_for
from flask import request
from ..csrf_token import enable_csrf, validate_csrf

from .utils import is_account_available


@auth.route("/signup", methods=["GET", "POST"])
def create_account():
    enable_csrf()

    if request.method == "POST":
        all_field = False

        for field in ["username", "tag", "age", "email", "password", "gender"]:
            if request.form.get(field) is None:
                all_field = False
                break
            all_field = True

        username = request.form.get("username")
        tag = request.form.get("tag")

        if validate_csrf() and all_field and is_account_available(username, tag):
            return redirect(url_for("auth.account_verification"))
        else:
            return "Invalid form data"

    return render_template("signup.html", csrf_token=session["csrf_token"])


@auth.route("/account/verification")
def account_verification():
    return render_template("email-verification.html")
