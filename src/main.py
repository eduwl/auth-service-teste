from fastapi import FastAPI, APIRouter, Request
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from src.controller.factory import create_login_controller
from src.middlewares.role_based import check_role

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

login_controller = create_login_controller()
app.include_router(login_controller.router)

router = APIRouter(prefix="/fake")

@router.get("/admin")
@check_role("admin")
async def admin_route(request: Request):
    return { "message": "Hello Admin!" }

@router.get("/user")
@check_role("user")
async def admin_route(request: Request):
    return { "message": "Hello User!" }

@router.get("/health")
async def public_route():
    return {"message": "OK!"}

app.include_router(router)