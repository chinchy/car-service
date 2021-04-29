from flask import render_template
from wtforms.csrf.core import CSRFTokenField


def render_table_template(template, title, model, data):

    return render_template(template,
                           title=title,
                           menu=(('Автомобили', 'cars'), ('Мастера', 'masters'),
                                 ('Услуги', 'services'), ('Журнал работ', 'works')),
                           header=(x.comment for x in model.__table__.columns),
                           fields=model.__table__.columns.keys(),
                           data=data)


def render_form_template(template, title, model, form):
    fields = []
    for key, item in form._fields.items():
        if type(item) is not CSRFTokenField:
            fields.append(key)

    return render_template(template,
                           title=title,
                           menu=(('Автомобили', 'cars'), ('Мастера', 'masters'),
                                 ('Услуги', 'services'), ('Журнал работ', 'works')),
                           form=form,
                           fields=fields)
