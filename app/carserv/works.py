from flask import Blueprint, flash, redirect, render_template, url_for

from app.db import db
from .forms import WorkForm
from .models import Work
from .utils import render_form_template

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


@bp.route('/edit/<int:model_id>', methods=['GET', 'POST'])
def edit(model_id):
    form = WorkForm()
    model = db.session.query(Work).filter(Work.id == model_id).first()

    if form.validate_on_submit():
        try:
            model.date_work = form.date_work.data
            model.master = form.master.data
            model.car = form.car.data
            model.service = form.service.data

            db.session.add(model)
            db.session.commit()

            flash('Запись успешно изменена!', category='success')
        except Exception as e:
            flash('Ошибка изменения записи: ' + str(e).replace('<', '&lt;').replace('>', '&gt;'), category='error')

        return redirect(url_for(".index"))

    form.date_work.data = model.date_work
    form.master.data = model.master
    form.car.data = model.car
    form.service.data = model.service

    return render_form_template('edit.html',
                                title='Журнал работ',
                                form=form)


@bp.route('/create', methods=['GET', 'POST'])
def create():
    form = WorkForm()

    if form.validate_on_submit():
        try:
            model = Work()
            model.date_work = form.date_work.data
            model.master = form.master.data
            model.car = form.car.data
            model.service = form.service.data

            db.session.add(model)
            db.session.commit()

            flash('Запись успешно создана!', category='success')
        except Exception as e:
            flash('Ошибка создания записи: ' + str(e).replace('<', '&lt;').replace('>', '&gt;'), category='error')

        return redirect(url_for(".index"))

    return render_form_template('create.html',
                                title='Журнал работ',
                                form=form)


@bp.route('/delete/<int:model_id>', methods=['GET', 'POST'])
def delete(model_id):
    try:
        model = db.session.query(Work).filter(Work.id == model_id).first()
        db.session.delete(model)
        db.session.commit()
        flash('Запись успешно удалена!', category='success')
    except Exception as e:
        flash('Ошибка удаления записи: ' + str(e).replace('<', '&lt;').replace('>', '&gt;'), category='error')

    return redirect(url_for(".index"))
