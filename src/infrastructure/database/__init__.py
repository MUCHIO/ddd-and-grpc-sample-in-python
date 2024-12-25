from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from sqlalchemy.orm import scoped_session

@contextmanager
def session_scope(database_url: str):
    engine = create_engine(database_url)
    session = scoped_session(sessionmaker(engine))
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()