import jwt
from fastapi import Request, HTTPException
from fastapi.routing import APIRoute
from typing import Callable
from functools import wraps

from src.utils import verify_token

SECRET_KEY = "supersecret"

def check_role(role: str):
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(request: Request, *args, **kwargs):
            auth_header = request.headers.get("Authorization")
            if not auth_header or not auth_header.startswith("Bearer"):
                raise HTTPException(status_code=401, detail="Unauthorized")

            token = auth_header.split(" ")[1]
            try:
                claims = verify_token(token)
                print(claims)
                user_role = claims["role"]
                print(role)
                if user_role != role:
                    raise HTTPException(status_code=403, detail="Access Forbidden: role permission error")

            except HTTPException:
                raise
            except Exception:
                raise HTTPException(status_code=401, detail="Unauthorized")

            return await func(request, *args, **kwargs)

        return wrapper
    return decorator