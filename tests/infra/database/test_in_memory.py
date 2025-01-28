from src.infra import InMemoryDatabase

def test_query_success():
    db = InMemoryDatabase()

    query = "SELECT * FROM users"
    rows = db.query(query)

    assert(len(rows) == 2)

def test_query_row_success():
    db = InMemoryDatabase()

    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    row = db.query_row(query, ("user", "L0XuwPOdS5U"))

    assert(row['username'] == 'user')
    assert(row['role'] == 'user')
    assert(row['password'] == 'L0XuwPOdS5U')