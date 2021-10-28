from pydantic import BaseSettings


class Settings(BaseSettings):
    DB_DSN: str = "postgresql://postgres:postgres@postgres:5432/postgres"
    APM_NAME: str = "test_app"
    APM_SERVER: str = "http://apm-server:8200"


settings = Settings()
