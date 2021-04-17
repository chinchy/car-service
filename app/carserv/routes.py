from flask import Blueprint

from app.db import db
from .models import Car

bp = Blueprint('carserv', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    q = db.session.query(Car.id).all()
    return "Cars id: " + ", ".join(map(lambda x: str(x[0]), q))
