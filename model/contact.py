from sys import maxsize

class Contact:

    def __init__(self, first_name=None, last_name=None, company=None, address=None, phone_home=None, mobilephone=None,
                 workphone=None, secondaryphone=None, e_mail=None, year=None, address_1=None, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.address = address
        self.phone_home = phone_home
        self.mobilephone = mobilephone
        self.secondaryphone = secondaryphone
        self.workphone = workphone
        self.e_mail = e_mail
        self.year = year
        self.address_1 = address_1
        self.id = id

    def __repr__(self):
        return "%s:%s %s " % (self.id, self.first_name, self.last_name,)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)\
               and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
