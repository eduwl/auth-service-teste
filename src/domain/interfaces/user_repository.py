from src.domain.model.user import User

class UserRepository:
    def find(self, username: str, password: str) -> User:
        raise NotImplementedError("Must implement find")