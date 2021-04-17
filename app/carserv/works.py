from flask import Blueprint

from app.db import db
from .models import Work
from .utils import render_table_template

bp = Blueprint('works', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_table_template('base.html',
                                 title='Журнал работ',
                                 model=Work,
                                 data=db.session.query(Work).order_by(Work.date_work.desc()).all())
