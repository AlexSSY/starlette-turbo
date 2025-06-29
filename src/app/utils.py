from passlib.hash import bcrypt

from . import settings


def hash_password(plain_password):
    return bcrypt.hash(plain_password + settings.SECRET_KEY)


def check_password(plain_password, hashed_password):
    return bcrypt.verify(plain_password + settings.SECRET_KEY, hashed_password)
