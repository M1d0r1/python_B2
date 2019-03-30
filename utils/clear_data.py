def test_helper_clear_groups(db):
    cursor = db.connection.cursor()
    cursor.execute("DELETE FROM group_list")
    cursor.close()


def test_helper_clear_contacts(db):
    cursor = db.connection.cursor()
    cursor.execute("DELETE FROM addressbook")
    cursor.close()

def test_helper_clear_relations(db):
    cursor = db.connection.cursor()
    cursor.execute("DELETE FROM address_in_groups")
    cursor.close()
