
def test_phones_on_homepage(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    app.contact.get_contact_info_from_edit_page()
