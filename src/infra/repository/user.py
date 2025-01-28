from src.domain import UserRepository, User
from src.infra import Database

class UserRepositoryImpl(UserRepository):
    def __init__(self, database: Database):
        self.database = database

    def find(self, username, password) -> User:
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        row = self.database.query_row(query, (username, password))

        if not row:
            return None

        return User(username=row["username"], role=row["role"], password=row["password"])