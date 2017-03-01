class ContactHelper:

    def __init__(self,app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init contact creations
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.phone_home)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.e_mail)
        # choose birth date
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[13]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[13]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[2]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.year)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address_1)
        # submit contact creations
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()


    def edit_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_css_selector('[title="Edit"]').click()
        #init update
        wd.find_element_by_css_selector('[name="firstname"]').clear()
        wd.find_element_by_css_selector('[name="firstname"]').send_keys('Modyfikacja')
        #submit update
        wd.find_element_by_name("update").click()

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_css_selector('[name="selected[]"]').click()
        #submit update
        wd.find_element_by_css_selector('[value="Delete"]').click()
        wd.switch_to_alert().accept()

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_css_selector('[name="selected[]"]'))