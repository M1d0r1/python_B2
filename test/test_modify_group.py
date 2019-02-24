from model.group import Group

def test_modify_first_group(app):
    app.session.login(admin="admin", password="secret")
    group = app.group.get_data_first()
    # Prepare data
    group.name = group.name + " upd"
    group.header = group.header + " upd"
    group.footer = group.footer + " upd"
    # Modify the group
    app.group.modify_first(group)
    app.session.logout()

def test_modify_first_group_name(app):
    app.session.login(admin="admin", password="secret")
    # Modify the group
    app.group.modify_first(Group(name="Only name"))
    app.session.logout()