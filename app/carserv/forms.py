from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, DecimalField, DateField
from wtforms_sqlalchemy.fields import QuerySelectField
from wtforms.widgets import Select
from wtforms.widgets.html5 import DateInput, NumberInput

from app.db import db
from .models import Car, Master, Service


class CarForm(FlaskForm):
    num = StringField('Гос. номер')
    color = StringField('Цвет')
    mark = StringField('Марка')
    is_foreign = BooleanField('Иномарка?')


class MasterForm(FlaskForm):
    name = StringField('ФИО')


class ServiceForm(FlaskForm):
    name = StringField('Наименование')
    cost_our = DecimalField('Стоимость для отечественных', widget=NumberInput())
    cost_foreign = DecimalField('Стоимость для импортных', widget=NumberInput())


class WorkForm(FlaskForm):
    date_work = DateField('Дата проведения работы', widget=DateInput())
    master = QuerySelectField('Мастер', allow_blank=True,
                              get_label=lambda m: m.name,
                              query_factory=lambda: db.session.query(Master).order_by(Master.name),
                              widget=Select())
    car = QuerySelectField('Автомобиль', allow_blank=True,
                           get_label=lambda m: '{} ({})'.format(m.num, m.mark),
                           query_factory=lambda: db.session.query(Car).order_by(Car.id),
                           widget=Select())
    service = QuerySelectField('Услуга', allow_blank=True,
                               get_label=lambda m: m.name,
                               query_factory=lambda: db.session.query(Service).order_by(Service.id),
                               widget=Select())
