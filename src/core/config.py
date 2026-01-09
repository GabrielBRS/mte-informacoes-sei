from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "MTE - Processamento SEI"
    API_V1_STR: str = "/api/v1"

    TERADATA_HOST: str
    TERADATA_USER: str
    TERADATA_PASS: str

    REDIS_HOST: str = "localhost"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True
    )


settings = Settings()