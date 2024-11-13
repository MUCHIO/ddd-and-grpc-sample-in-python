from pydantic_settings import BaseSettings, SettingsConfigDict
import os

def _is_pytest_running():
    return os.environ.get("PYTEST_VERSION") is not None

class Settings(BaseSettings):
    db_driver: str
    db_user: str
    db_password: str
    db_host: str
    db_port: str
    db_name: str

    @property
    def modified_db_name(self) -> str:
        if _is_pytest_running():
            return f"{self.db_name}_test"
        return self.db_name

    @property
    def database_url(self) -> str:
        return f"{self.db_driver}://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.modified_db_name}"

    model_config = SettingsConfigDict(env_file = '.env', env_file_encoding='utf-8')

settings = Settings()