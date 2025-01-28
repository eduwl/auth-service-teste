from fastapi import APIRouter, HTTPException
from typing import Dict
from pydantic import BaseModel, Field
from src.domain import UseCase, UserNotFound

class LoginPayload(BaseModel):
    username: str = Field(..., title="Username", description="User login name")
    password: str = Field(..., title="Password", description="User login password")

class LoginController:
    def __init__(self, usecase: UseCase):
        self.usecase = usecase
        self.router = APIRouter(prefix="/fake")
        self.router.post("/token")(self.handler)
    
    async def handler(self, payload: LoginPayload):
        try:
            if not payload.username or not payload.password:
                raise HTTPException(status_code=400, detail="Missing login information")
            
            token = self.usecase.execute(payload.model_dump())

            return {"token": token}
        except UserNotFound:
            raise HTTPException(status_code=401, detail="Unauthorized")
        except HTTPException as e:
            raise
        except Exception as e:
            print(f"LoginController: {e}")
            raise HTTPException(status_code=500, detail="Internal Serve Error")