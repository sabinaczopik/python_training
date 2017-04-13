from sys import maxsize

class Contact:

    def __init__(self, first_name=None, last_name=None, company=None, address=None, address2=None, phone_home=None,
                 mobilephone=None, workphone=None, secondaryphone=None, all_phones_from_home_page=None, e_mail=None,
                 e_mail_2=None, email_3=None, year=None,all_email_from_home_page=None, id=None,
                 all_addresses_from_home_page=None):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.address = address
        self.address2 = address2
        self.all_addresses_from_home_page = all_addresses_from_home_page
        self.phone_home = phone_home
        self.mobilephone = mobilephone
        self.secondaryphone = secondaryphone
        self.workphone = workphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.e_mail = e_mail
        self.e_mail_2 = e_mail_2
        self.e_mail_3 = email_3
        self.all_email_from_home_page = all_email_from_home_page
        self.year = year
        self.id = id

    def __repr__(self):
        return "%s:%s %s %s" % (self.id, self.first_name, self.last_name, self.company)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
               and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
