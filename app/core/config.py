from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "App"
    database_url: str
    debug: bool = False
    log_level: str = "INFO"
    log_file_path: str = "logs/app.log"
    log_max_bytes: int = 10 * 1024 * 1024
    log_backup_count: int = 5

    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()