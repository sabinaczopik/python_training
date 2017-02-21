
def test_edit_contact(app):
    app.session.log_in(username="admin", password="secret")
    app.contact.edit_first_contact()
    app.session.log_out()