from flask import Blueprint, flash, redirect, url_for

from app.db import db
from .forms import ServiceForm
from .models import Service
from .utils import render_table_template, render_form_template

bp = Blueprint('services', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_table_template('index.html',
                                 title='Услуги',
                                 model=Service,
                                 data=db.session.query(Service).order_by(Service.id).all())


@bp.route('/edit/<int:model_id>', methods=['GET', 'POST'])
def edit(model_id):
    form = ServiceForm()
    model = db.session.query(Service).filter(Service.id == model_id).first()

    if form.validate_on_submit():
        try:
            model.name = form.name.data
            model.cost_our = form.cost_our.data
            model.cost_foreign = form.cost_foreign.data

            db.session.add(model)
            db.session.commit()

            flash('Запись успешно изменена!', category='success')
        except Exception as e:
            flash('Ошибка изменения записи! ' + str(e).replace('<', '&lt;').replace('>', '&gt;'), category='error')

        return redirect(url_for(".index"))

    form.name.data = model.name
    form.cost_our.data = model.cost_our
    form.cost_foreign.data = model.cost_foreign

    return render_form_template('edit.html',
                                title='Услуги',
                                model=Service,
                                form=form)


@bp.route('/create', methods=['GET', 'POST'])
def create():
    form = ServiceForm()

    if form.validate_on_submit():
        try:
            model = Service()
            model.name = form.name.data
            model.cost_our = form.cost_our.data
            model.cost_foreign = form.cost_foreign.data

            db.session.add(model)
            db.session.commit()

            flash('Запись успешно создана!', category='success')
        except Exception as e:
            flash('Ошибка создания записи! ' + str(e).replace('<', '&lt;').replace('>', '&gt;'), category='error')

        return redirect(url_for(".index"))

    return render_form_template('create.html',
                                title='Услуги',
                                model=Service,
                                form=form)


@bp.route('/delete/<int:model_id>', methods=['GET', 'POST'])
def delete(model_id):
    try:
        model = db.session.query(Service).filter(Service.id == model_id).first()
        db.session.delete(model)
        db.session.commit()
        flash('Запись успешно удалена!', category='success')
    except Exception as e:
        flash('Ошибка удаления записи: ' + str(e).replace('<', '&lt;').replace('>', '&gt;'), category='error')

    return redirect(url_for(".index"))
