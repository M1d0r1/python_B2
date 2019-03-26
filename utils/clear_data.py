def test_helper_clear_groups(app, db):
    cursor = db.connection.cursor()
    cursor.execute("DELETE FROM group_list")
    cursor.close()


def test_helper_clear_contacts(app, db):
    cursor = db.connection.cursor()
    cursor.execute("DELETE FROM addressbook")
    cursor.close()
