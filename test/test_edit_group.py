from model.group import Group


def test_edit_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer= "footer group"))
    app.group.edit_first_group(Group(name="New Group"))



def test_edit_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="test", footer= "footer group"))
    app.group.edit_first_group(Group(header="New header"))
