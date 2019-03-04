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
    old_groups = app.group.get_group_list()
    app.group.modify_first(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_first_group_name(app):
    # Modify the group
    if app.group.count() == 0:
        app.group.create(Group(name = "Group for modification"))
    old_groups = app.group.get_group_list()
    app.group.modify_first(Group(name="Only name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)