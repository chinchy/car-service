import app


class Base(object):
    SECRET_KEY = 'fkvnjfkdvndfklvndfzvn;lkf'
    SQLALCHEMY_DATABASE_URI = 'postgresql://ilya@localhost/carserv'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_APP = app
