from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "Group for modification"))
    group = app.group.get_data_first()
    # Prepare data
    group.name = group.name + " upd"
    group.header = group.header + " upd"
    group.footer = group.footer + " upd"
    old_groups = app.group.get_group_list()
    group.id = old_groups[0].id
    # Modify the group
    app.group.modify_first(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)

def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name = "Group for modification"))
    old_groups = app.group.get_group_list()
    group = Group(name="Only name")
    group.id = old_groups[0].id
    # Modify the group
    app.group.modify_first(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key = Group.id_or_max) == sorted(new_groups, key = Group.id_or_max)