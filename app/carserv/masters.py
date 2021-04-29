from flask import Blueprint, flash, redirect, url_for

from app.db import db
from .forms import MasterForm
from .models import Master
from .utils import render_table_template, render_form_template

bp = Blueprint('masters', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    return render_table_template('index.html',
                                 title='Мастера',
                                 model=Master,
                                 data=db.session.query(Master).order_by(Master.id).all())


@bp.route('/edit/<int:model_id>', methods=['GET', 'POST'])
def edit(model_id):
    form = MasterForm()
    model = db.session.query(Master).filter(Master.id == model_id).first()

    if form.validate_on_submit():
        try:
            model.name = form.name.data
            db.session.add(model)
            db.session.commit()
            flash('Запись успешно изменена!', category='success')
        except Exception as e:
            flash('Ошибка изменения записи: ' + str(e).replace('<', '&lt;').replace('>', '&gt;'), category='error')

        return redirect(url_for(".index"))

    form.name.data = model.name

    return render_form_template('edit.html',
                                title='Мастера',
                                form=form)


@bp.route('/create', methods=['GET', 'POST'])
def create():
    form = MasterForm()

    if form.validate_on_submit():
        try:
            model = Master()
            model.name = form.name.data
            db.session.add(model)
            db.session.commit()
            flash('Запись успешно создана!', category='success')
        except Exception as e:
            flash('Ошибка создания записи: ' + str(e).replace('<', '&lt;').replace('>', '&gt;'), category='error')

        return redirect(url_for(".index"))

    return render_form_template('create.html',
                                title='Мастера',
                                form=form)


@bp.route('/delete/<int:model_id>', methods=['GET', 'POST'])
def delete(model_id):
    try:
        model = db.session.query(Master).filter(Master.id == model_id).first()
        db.session.delete(model)
        db.session.commit()
        flash('Запись успешно удалена!', category='success')
    except Exception as e:
        flash('Ошибка удаления записи: ' + str(e).replace('<', '&lt;').replace('>', '&gt;'), category='error')

    return redirect(url_for(".index"))
