from datetime import datetime, timezone
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.orm import declarative_base, declared_attr


Base = declarative_base()


def current_datetime():
    return datetime.now(timezone.utc)


class CommonFieldsMixin:
    id = Column(Integer, primary_key=True, autoincrement=True)

    @declared_attr
    def created_at(cls):
        return Column(DateTime, nullable=False, default=current_datetime)
    
    @declared_attr
    def updated_at(cls):
        return Column(DateTime, nullable=False, default=current_datetime, onupdate=current_datetime)


class User(CommonFieldsMixin, Base):
    __tablename__ = "users"
    
    username = Column(String(length=20), unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
