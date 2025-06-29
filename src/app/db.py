from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///db.sqlite", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(engine, autoflush=False, autocommit=False)


def create_db(decl_base_class):
    decl_base_class.metadata.create_all(engine)


def drop_db(decl_base_class):
    decl_base_class.metadata.drop_all(engine)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


def get_next_session():
    return next(get_session())
