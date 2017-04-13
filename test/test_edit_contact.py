from model.contact import Contact
from random import randrange


def test_edit_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name ="Sabina", last_name="test", company="Pewex",
                                   address="osiedle", phone_home="123456789", e_mail="sabina@sabina.pl",
                                   year="2016",))
    old_contact = db.get_contact_list()
    index = randrange(len(old_contact))
    contact = Contact(first_name='Kasia', last_name='Bober')
    contact.id = old_contact[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contact) == app.contact.count()
    new_contact = db.get_contact_list()
    old_contact[index] = contact
    assert old_contact == new_contact
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(
            app.group.get_contact_list(), key=Contact.id_or_max
        )