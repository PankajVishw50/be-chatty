from flask import Blueprint

auth = Blueprint("auth", __name__)

from .views import *
from .api import *