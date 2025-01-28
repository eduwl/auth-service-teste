from datetime import datetime, timedelta, UTC
import jwt
import os

def create_token(claims: dict[str, str], expires_in: int = 3600) -> str:
    SECRETY_KEY=os.getenv("SECRETY_KEY")

    payload = claims.copy()
    payload["exp"] = datetime.now(UTC) + timedelta(seconds=expires_in)
    return jwt.encode(payload, SECRETY_KEY, algorithm="HS256")

def verify_token(token: str) -> dict:
    SECRETY_KEY=os.getenv("SECRETY_KEY")

    try:
        decoded = jwt.decode(token, SECRETY_KEY, algorithms=["HS256"])
        return decoded
    except jwt.ExpiredSignatureError:
        raise ValueError("O token expirou")
    except jwt.InvalidTokenError:
        raise ValueError("Token inválido")