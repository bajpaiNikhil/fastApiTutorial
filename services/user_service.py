from data.user import User


def user_count():
    return 254_030


def create_account(name: str, email: str, password: str) -> User:
    return User(name, email, "fbihbvis")
