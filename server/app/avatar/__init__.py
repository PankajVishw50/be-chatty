from flask import Blueprint

avatar = Blueprint("avatar", __name__)

from .views import *
from .api import *