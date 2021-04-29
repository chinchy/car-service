from flask import Blueprint, redirect, flash, url_for

from app.db import db
from .models import Car
from .utils import render_table_template

bp = Blueprint('cars', __name__)


@bp.route('/', methods=['GET', 'POST'])
def home():
    return redirect("cars")


@bp.route('/cars', methods=['GET', 'POST'])
def index():
    return render_table_template('index.html',
                                 title='Автомобили',
                                 model=Car,
                                 data=db.session.query(Car).order_by(Car.id).all())
