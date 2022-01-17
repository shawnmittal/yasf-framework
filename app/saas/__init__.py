from flask import Blueprint

bp = Blueprint('saas', __name__)

from app.saas import routes