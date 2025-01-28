from unittest.mock import Mock
from src.infra import UserRepositoryImpl

def test_find():
    mock_db = Mock()
    mock_db.query_row.return_value = {"username": "eduwl", "role": "admin", "password": "teste123"}

    user_repository = UserRepositoryImpl(mock_db)
    user = user_repository.find("eduwl", "teste123")

    assert(user.username == "eduwl")
    assert(user.role == "admin")
    assert(user.password == "teste123")

def test_find_none():
    mock_db = Mock()
    mock_db.query_row.return_value = {}

    user_repository = UserRepositoryImpl(mock_db)
    user = user_repository.find("eduwl", "teste123")

    assert(user == None)
    assert(not user)