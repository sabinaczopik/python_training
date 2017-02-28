# -*- coding: utf-8 -*-

from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="test", header="test2", footer="test3"))

def test_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
