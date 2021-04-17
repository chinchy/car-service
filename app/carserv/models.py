from app.db import db


class Car(db.Model):

    __tablename__ = 'cars'

    id = db.Column(db.Integer, comment='#', primary_key=True)
    num = db.Column(db.String(9), comment='Гос. номер')
    color = db.Column(db.String(20), comment='Цвет')
    mark = db.Column(db.String(20), comment='Марка')
    is_foreign = db.Column(db.Boolean, comment='Иномарка?')


class Master(db.Model):

    __tablename__ = 'masters'

    id = db.Column(db.Integer, comment='#', primary_key=True)
    name = db.Column(db.String(50), comment='ФИО')


class Service(db.Model):

    __tablename__ = 'services'

    id = db.Column(db.Integer, comment='#', primary_key=True)
    name = db.Column(db.String(50), comment='Наименование')
    cost_our = db.Column(db.Numeric(18, 2), comment='Стоимость для отечественных')
    cost_foreign = db.Column(db.Numeric(18, 2), comment='Стоимость для импортных')


class Work(db.Model):

    __tablename__ = 'works'

    id = db.Column(db.Integer, comment='#', primary_key=True)
    date_work = db.Column(db.Date, comment='Дата проведения работы')
    master_id = db.Column(db.Integer, db.ForeignKey(Master.id), comment='Мастер')
    car_id = db.Column(db.Integer, db.ForeignKey(Car.id), comment='Автомобиль')
    service_id = db.Column(db.Integer, db.ForeignKey(Service.id), comment='Услуга')
