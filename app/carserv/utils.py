from flask import render_template


def render_table_template(template, title, model, data):

    return render_template(template,
                           title=title,
                           menu=(('Автомобили', 'cars'), ('Мастера', 'masters'),
                                 ('Услуги', 'services'), ('Журнал работ', 'works')),
                           header=(x.comment for x in model.__table__.columns),
                           fields=model.__table__.columns.keys(),
                           data=data)
