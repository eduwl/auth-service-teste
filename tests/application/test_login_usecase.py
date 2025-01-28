import pytest
from unittest.mock import Mock

from src.domain import User, UserNotFound
from src.application import LoginUseCase 
from src.utils import verify_token

def test_execute():
    mock_repo = Mock()
    mock_repo.find.return_value = User(username="eduwl", role="admin", password="teste123")

    usecase =  LoginUseCase(repository=mock_repo)
    token = usecase.execute({"username": "eduwl", "password": "teste123"})

    assert(token is not None)

    claims = verify_token(token)

    assert(claims["username"] == "eduwl")
    assert(claims["role"] == "admin")

def test_execute_fail():
    mock_repo = Mock()
    mock_repo.find.return_value = None

    usecase =  LoginUseCase(repository=mock_repo)
    with pytest.raises(UserNotFound, match="user not found"):
        usecase.execute({"username": "eduwl", "password": "teste123"})