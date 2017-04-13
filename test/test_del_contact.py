from model.contact import Contact
import random


def test_delete_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name ="Sabina", last_name="test", company="Pewex",
                               address="osiedle", phone_home="123456789", e_mail="sabina@sabina.pl",
                               year="2016"))
    old_contact = db.get_contact_list()
    contact = random.choice(old_contact)
    app.contact.delete_contact_by_id(contact.id)
    assert len(old_contact) - 1 == app.contact.count()
    new_contact = db.get_contact_list()
    old_contact.remove(contact)
    assert old_contact == new_contact
    if check_ui:
        assert sorted(new_contact, key=Contact.id_or_max) == sorted(
            app.contact.get_contact_list(), key=Contact.id_or_max
        )

