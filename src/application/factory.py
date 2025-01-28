from src.infra.factory import create_user_repository 
from src.application.login_usecase import LoginUseCase

def create_login_usecase():
    return LoginUseCase(repository=create_user_repository())