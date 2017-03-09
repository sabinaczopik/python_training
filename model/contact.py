from sys import maxsize

class Contact:

    def __init__(self,first_name=None, last_name=None, company=None, address=None, phone_home=None,
                 e_mail=None, year=None, address_1=None, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.address = address
        self.phone_home = phone_home
        self.e_mail = e_mail
        self.year = year
        self.address_1 = address_1
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.e_mail)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.e_mail == other.e_mail

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize