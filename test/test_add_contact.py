# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.contact import Contact


@pytest.fixture
def app(request):
    fixtura = Application()
    request.addfinalizer(fixtura.destroy)
    return fixtura

def test_add_contact(app):
    app.navigation.open_home_page()
    app.session.log_in(username = "admin", password = "secret")
    app.contact.create(Contact(first_name ="Sabina", last_name ="test", company ="Pewex",
                               address = "osiedle", phone_home = "123456789", e_mail = "sabina@sabina.pl",
                               year = "2016", address_1 = "Adress1"))
    app.navigation.return_to_homepage()
    app.session.log_out()

