class SessionHelper:


    def __init__(self,app):
        self.app = app

    def log_in(self, username, password):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_element_by_id("content").click()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector('input[type="submit"]').click()

    def log_out(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Logout").click()

    def ensure_log_out(self):
        if self.is_logged_in():
            self.log_out()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout")) > 0

    def ensure_log_in(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.log_out()
        self.log_in(username,password)

    def is_logged_in_as(self,username):
        # wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        return wd.find_element_by_xpath("//form/b").text[1:-1]