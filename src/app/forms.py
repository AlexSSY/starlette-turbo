from typing import Callable
from sqlalchemy.orm import Session
from .models import User
from .db import get_next_session


def min_len_validator(minimum=1):

    def validator(form, name, value):
        if len(value) < minimum:
            return "too short"
        
    return validator


def unique_validator(get_session_callback: Callable[[], Session]):

    def validator(form, name, value):
        session = get_session_callback()
        column = getattr(form.meta.model, name)
        if session.query(form.meta.model).filter(column == value).first() is not None:
            return "already exists"

    return validator


class BaseFormMeta(type):
    def __new__(cls, name, bases, namespace):
        new_class = super().__new__(cls, name, bases, namespace)
        return new_class


class SignupForm(metaclass=BaseFormMeta):
    class Meta:
        model = User

    def __init__(self, form_data):
        self.form_data = form_data
        self.errors = {}

    username = {
        "type": "text",
        "abstract": False,
        "validators": [
            min_len_validator(),
            unique_validator(get_next_session)
        ]
    }

    password = {
        "type": "password",
        "abstract": True,
        "validators": [
            min_len_validator(),
        ]
    }

    password_confirmation = {
        "type": "password",
        "abstract": True,
        "validators": []
    }

    def validate() -> bool:
        pass
