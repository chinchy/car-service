from .db import db
from .carserv import cars_bp, masters_bp, services_bp, works_bp

from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.Base')

    db.app = app
    db.init_app(app)

    app.register_blueprint(cars_bp, url_prefix='/')
    app.register_blueprint(masters_bp, url_prefix='/masters')
    app.register_blueprint(services_bp, url_prefix='/services')
    app.register_blueprint(works_bp, url_prefix='/works')

    return app
