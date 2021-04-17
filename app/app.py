from .db import db

from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.Base')

    db.app = app
    db.init_app(app)

    from .carserv import bp as carserv_bp
    app.register_blueprint(carserv_bp, url_prefix='/')

    return app
