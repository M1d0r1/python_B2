def test_delete_first_contact(app):
    app.session.login(admin="admin", password="secret")
    app.contact.delete_first()
    app.session.logout()