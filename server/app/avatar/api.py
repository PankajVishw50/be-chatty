from . import avatar
from .model import generate_multiavatar


@avatar.route("/api/avatar/<string:id>")
def get_avatar(id):
    _avatar = generate_multiavatar(id)
    return _avatar
