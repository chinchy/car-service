from flask import Blueprint

from app.db import db
from .models import Master
from .utils import render_table_template

bp = Blueprint('masters', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_table_template('base.html',
                                 title='Мастера',
                                 model=Master,
                                 data=db.session.query(Master).order_by(Master.id).all())
