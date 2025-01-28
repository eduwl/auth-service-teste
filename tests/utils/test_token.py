from dotenv import load_dotenv
import pytest
import jwt
import os

from src.utils.token import create_token, verify_token

load_dotenv()
SECRETY_KEY=os.getenv("SECRETY_KEY")

@pytest.fixture
def mock_claims():
    return {"user": "user", "role": "admin"}

def test_create_token(mock_claims):
    token = create_token(mock_claims)
    decoded = jwt.decode(token, SECRETY_KEY, algorithms=["HS256"])

    assert decoded["user"] == mock_claims["user"]
    assert decoded["role"] == mock_claims["role"]
    assert "exp" in decoded
    assert isinstance(decoded["exp"], int)


def test_verify_token_success(mock_claims):
    token = create_token(mock_claims)
    decoded = verify_token(token)

    assert decoded["user"] == mock_claims["user"]
    assert decoded["role"] == mock_claims["role"]

def test_verify_token_expired(mock_claims):
    token = create_token(mock_claims, expires_in=-1)

    with pytest.raises(ValueError, match="O token expirou"):
        verify_token(token)

def test_verify_token_invalid():
    token = "invalid_token"

    with pytest.raises(ValueError, match="Token inválido"):
        verify_token(token)