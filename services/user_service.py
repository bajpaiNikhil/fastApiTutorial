from typing import Optional

from data.user import User


def user_count():
    return 254_030


def create_account(name: str, email: str, password: str) -> User:
    return User(name, email, "abc")


def login_user(email: str, password: str) -> Optional[User]:
    if password == 'abc':
        return User("test user", email, 'abc')

    return None
