import re


def test_contact_details_on_homepage(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.all_email_from_home_page == merge_email_like_on_homepage(contact_from_edit_page)
    assert contact_from_homepage.all_addresses_from_home_page == merge_addresses_like_on_homepage(contact_from_edit_page)


def clear(s):
    return re.sub("[() - ]", "", s)


def merge_email_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.e_mail, contact.e_mail_2, contact.e_mail_3]
                                       ))))


def merge_addresses_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.address]
                                       ))))