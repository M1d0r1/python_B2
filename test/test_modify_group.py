from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "Group for modification"))
    group = app.group.get_data_first()
    # Prepare data
    group.name = group.name + " upd"
    group.header = group.header + " upd"
    group.footer = group.footer + " upd"
    # Modify the group
    app.group.modify_first(group)


def test_modify_first_group_name(app):
    # Modify the group
    if app.group.count() == 0:
        app.group.create(Group(name = "Group for modification"))
    app.group.modify_first(Group(name="Only name"))
