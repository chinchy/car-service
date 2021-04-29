from flask import Blueprint

from app.db import db
from .models import Work
from .utils import render_table_template

bp = Blueprint('works', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html',
                           title='Журнал работ',
                           menu=(('Автомобили', 'cars'), ('Мастера', 'masters'),
                                 ('Услуги', 'services'), ('Журнал работ', 'works')),
                           header=(x.comment for x in Work.__table__.columns),
                           fields=('id', 'date_work', 'master', 'car', 'service'),
                           data=db.session.query(Work).order_by(Work.date_work.desc()).all())
