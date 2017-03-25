import re


def test_phones_on_homepage(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.phone_home == clear(contact_from_edit_page.phone_home)
    assert contact_from_homepage.mobilephone == clear(contact_from_edit_page.mobilephone)
    assert contact_from_homepage.secondaryphone == clear(contact_from_edit_page.secondaryphone)
    assert contact_from_homepage.workphone == clear(contact_from_edit_page.workphone)

def test_phones_on_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.phone_home == contact_from_edit_page.phone_home
    assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone

def clear(s):
    return re.sub("[() -]", "", s)
