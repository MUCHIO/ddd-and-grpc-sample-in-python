import factory
from src.infrastructure.database.schemas.route import Route
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.config import settings
from sqlalchemy.orm import scoped_session

ENGINE = create_engine(
    settings.database_url,
    echo=False
)

scoped_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

class RouteFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Route
        sqlalchemy_session = scoped_session
        sqlalchemy_session_persistence = 'commit'

    name = factory.Faker('name')
    latitude = factory.Faker('random_int', min=1, max=100)
    longitude = factory.Faker('random_int', min=1, max=100)
