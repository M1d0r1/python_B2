from model.group import Group


def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    db_list = db.get_group_list()
    i=0
    for  i in range(0, len(db_list)):
        print (" ",db_list[i])
        db_list[i] = db_list[i].clear()
    assert sorted(ui_list, key = Group.id_or_max) == sorted(db_list, key = Group.id_or_max)