from src.infra import InMemoryDatabase, UserRepositoryImpl

def create_user_repository() -> UserRepositoryImpl:
    return UserRepositoryImpl(database=InMemoryDatabase())