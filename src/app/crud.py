from .models import User
from .db import SessionLocal
from .utils import hash_password, check_password


def create_user(username, password) -> User:
    with SessionLocal() as session:
        session.add(User(username=username, hashed_password=hash_password(password)))
        session.commit()


def get_user_by_id(id) -> User | None:
    with SessionLocal() as session:
        return session.get(User, id)


def authenticate_user(username, password) -> User | None:
    with SessionLocal() as session:
        user = session.query(User).filter(User.username == username).first()
    if user is not None and check_password(password, user.hashed_password):
        return user
    return None


def list_users(offset=0, limit=10):
    with SessionLocal() as session:
        return session.query(User).offset(offset).limit(limit).all()
