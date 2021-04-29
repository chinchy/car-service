from flask import Blueprint, redirect, flash, url_for

from app.db import db
from .forms import CarForm
from .models import Car
from .utils import render_table_template, render_form_template

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


@bp.route('/cars/edit/<int:model_id>', methods=['GET', 'POST'])
def edit(model_id):
    form = CarForm()
    model = db.session.query(Car).filter(Car.id == model_id).first()

    if form.validate_on_submit():
        try:
            model.num = form.num.data
            model.color = form.color.data
            model.mark = form.mark.data
            model.is_foreign = form.is_foreign.data

            db.session.add(model)
            db.session.commit()

            flash('Запись успешно изменена!', category='success')
        except Exception as e:
            flash('Ошибка изменения записи: ' + str(e).replace('<', '&lt;').replace('>', '&gt;'), category='error')

        return redirect(url_for(".index"))

    form.num.data = model.num
    form.color.data = model.color
    form.mark.data = model.mark
    form.is_foreign.data = model.is_foreign

    return render_form_template('edit.html',
                                title='Автомобили',
                                model=Car,
                                form=form)


@bp.route('/cars/create', methods=['GET', 'POST'])
def create():
    form = CarForm()

    if form.validate_on_submit():
        try:
            model = Car()
            model.num = form.num.data
            model.color = form.color.data
            model.mark = form.mark.data
            model.is_foreign = form.is_foreign.data

            db.session.add(model)
            db.session.commit()

            flash('Запись успешно создана!', category='success')
        except Exception as e:
            flash('Ошибка создания записи: ' + str(e).replace('<', '&lt;').replace('>', '&gt;'), category='error')

        return redirect(url_for(".index"))

    return render_form_template('create.html',
                                title='Автомобили',
                                model=Car,
                                form=form)


@bp.route('/cars/delete/<int:model_id>', methods=['GET', 'POST'])
def delete(model_id):
    try:
        model = db.session.query(Car).filter(Car.id == model_id).first()
        db.session.delete(model)
        db.session.commit()
        flash('Запись успешно удалена!', category='success')
    except Exception as e:
        flash('Ошибка удаления записи: ' + str(e).replace('<', '&lt;').replace('>', '&gt;'), category='error')

    return redirect(url_for(".index"))
