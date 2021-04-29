from flask import Blueprint

from app.db import db
from .models import Service
from .utils import render_table_template

bp = Blueprint('services', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_table_template('index.html',
                                 title='Услуги',
                                 model=Service,
                                 data=db.session.query(Service).order_by(Service.id).all())
