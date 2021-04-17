from app.db import db


class Car(db.Model):

    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.String(9))
    color = db.Column(db.String(20))
    mark = db.Column(db.String(20))
    is_foreign = db.Column(db.Boolean)


class Master(db.Model):

    __tablename__ = 'masters'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))


class Service(db.Model):

    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    cost_our = db.Column(db.Numeric(18, 2))
    cost_foreign = db.Column(db.Numeric(18, 2))


class Work(db.Model):

    __tablename__ = 'works'

    id = db.Column(db.Integer, primary_key=True)
    date_work = db.Column(db.Date)
    master_id = db.Column(db.Integer, db.ForeignKey(Master.id))
    car_id = db.Column(db.Integer, db.ForeignKey(Car.id))
    service_id = db.Column(db.Integer, db.ForeignKey(Service.id))
