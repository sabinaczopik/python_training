from fixture.orm import ORMFixture
from fixture.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = list(db. get_contacts_in_group(Group(id="52")))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass # db.destroy()
