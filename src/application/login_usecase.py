from typing import Dict

from src.domain import UseCase, UserRepository, UserNotFound
from src.utils import create_token

class LoginUseCase(UseCase):
    def __init__(self, repository: UserRepository):
        self.repository = repository
    
    def execute(self, input: Dict[str, str]) -> str:
        user = self.repository.find(input["username"], input["password"])
        
        if not user:
            raise UserNotFound(message="user not found")
        
        claims = {"username": user.username, "role": user.role}

        return  create_token(claims)