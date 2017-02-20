# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.session.log_in(username="admin", password="secret")
    app.group.create(Group(name="test", header="test2", footer="test3"))
    app.session.log_out()

def test_empty_group(app):
    app.session.log_in(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.log_out()
