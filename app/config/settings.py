# app/config/settings.py
from pydantic_settings  import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FAPIN"
    debug: bool = True
    host: str = "127.0.0.1"
    port: int = 8000

    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str

    class Config:
        env_file = ".env"
    
    @property
    def db_url(self):
        return (
            f"mysql+aiomysql://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )
settings = Settings()
