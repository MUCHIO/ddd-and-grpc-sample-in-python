import factory
from src.infrastructure.database.schemas.route import Route
from src.infrastructure.database import Session

class RouteFactory(factory.alchemy.SQLAlchemyModelFactory):
    class Meta:
        model = Route
        sqlalchemy_session = Session()
        sqlalchemy_session_persistence = 'commit'

    name = factory.Faker('name')
    latitude = factory.Faker('random_int', min=1, max=100)
    longitude = factory.Faker('random_int', min=1, max=100)
