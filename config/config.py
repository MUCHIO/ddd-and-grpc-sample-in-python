from pydantic_settings import BaseSettings
from pydantic import ConfigDict
import sys

def is_pytest_running():
    return 'pytest' in sys.argv[0]

class Settings(BaseSettings):
    database_url: str
    model_config = ConfigDict(env_file = '.env.test' if is_pytest_running() else '.env' )

settings = Settings()