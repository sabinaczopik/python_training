from model.contact import Contact

def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name ="Sabina", last_name="test", company="Pewex",
                               address="osiedle", phone_home="123456789", e_mail="sabina@sabina.pl",
                               year ="2016", address_1="Adress1"))
    app.contact.delete_first_contact()

