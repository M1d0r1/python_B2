from model.group import Group

def test_modify_first_contact(app):
    app.session.login(admin="admin", password="secret")

    app.contact.modify_first()
    app.session.logout()