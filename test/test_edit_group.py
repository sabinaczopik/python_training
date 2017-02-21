def test_edit_first_group(app):
    app.session.log_in(username="admin", password="secret")
    app.group.edit_first_group()
    app.session.log_out()