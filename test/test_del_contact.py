
def test_delete_contact(app):
    app.contact.delete_first_contact()
    app.session.log_out()
