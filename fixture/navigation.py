class NavigationHelper:


    def __init__(self,app):
        self.app = app


    def return_to_homepage(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()


    def open_home_page(self,):
        wd = self.app.wd
        wd.get("http://localhost/addressbook/")