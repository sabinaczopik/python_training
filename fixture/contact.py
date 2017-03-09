from model.contact import Contact

class ContactHelper:

    def __init__(self,app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init contact creations
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        # submit contact creations
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.first_name)
        self.change_field_value("lastname", contact.last_name)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.phone_home)
        self.change_field_value("email", contact.e_mail)
        # choose birth date
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[13]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[13]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
        self.change_field_value("byear",contact.year)
        self.change_field_value("address2", contact.address_1)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_css_selector('[title="Edit"]').click()
        # init update
        self.fill_contact_form(new_contact_data)
        # submit update
        wd.find_element_by_name("update").click()
        wd.find_element_by_css_selector('[href="./"]').click()
        self.contact_cache = None

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_css_selector('[name="selected[]"]').click()
        # submit update
        wd.find_element_by_css_selector('[value="Delete"]').click()
        wd.switch_to_alert().accept()
        wd.find_element_by_css_selector('[href="./"]').click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_css_selector('[name="selected[]"]'))

    contact_cache = None
    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector('tr[name="entry"]'):
                email = element.find_element_by_name("selected[]").get_attribute("accept")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(e_mail=email, id=id))
        return list(self.contact_cache)
