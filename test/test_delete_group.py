def test_delete_first_group(app):
    app.session.login(admin="admin", password="secret")
    # Delete the group
    app.group.delete_first()
    app.session.logout()