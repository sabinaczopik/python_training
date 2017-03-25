from model.contact import Contact
from random import randrange


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name ="Sabina", last_name="test", company="Pewex",
                                   address="osiedle", phone_home="123456789", e_mail="sabina@sabina.pl",
                                   year="2016", address_1="Adress1"))
    old_contact = app.contact.get_contact_list()
    index = randrange(len(old_contact))
    # contact = Contact(e_mail="sksk@kf.pl")
    contact = Contact(first_name='Kasia', last_name='Bober')
    contact.id = old_contact[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contact) == app.contact.count()
    new_contact = app.contact.get_contact_list()
    old_contact[index] = contact
    assert sorted(old_contact, key=Contact.id_or_max) == sorted(new_contact, key=Contact.id_or_max)
