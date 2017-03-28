# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name ="Sabina", last_name ="test", company ="Pewex",
                               address = "osiedle", phone_home = "123456789", e_mail="sabina@sabina.pl",
                               year = "2016", address2 = "Adress1", mobilephone='12355', secondaryphone='2568964',
                               workphone='45866633')
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

