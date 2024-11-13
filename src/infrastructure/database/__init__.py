from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.config import settings
from contextlib import contextmanager
from sqlalchemy.orm import scoped_session

engine = create_engine(settings.database_url)

@contextmanager
def session_scope():
    session = scoped_session(sessionmaker(engine))
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()