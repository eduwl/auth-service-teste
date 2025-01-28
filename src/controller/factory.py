from src.application.factory import create_login_usecase
from src.controller.login import LoginController

def create_login_controller():
    return LoginController(usecase=create_login_usecase())