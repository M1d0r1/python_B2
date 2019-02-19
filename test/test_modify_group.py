def test_modify_first_group(app):
    app.session.login(admin="admin", password="secret")
    # Set the index in order to distinguish the created groups
    app.group.modify_first()
    app.session.logout()