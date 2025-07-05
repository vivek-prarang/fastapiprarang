from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from app.config.settings import settings
 

db_url = settings.db_url
engine: Engine = create_engine(db_url, pool_pre_ping=True)


def db_conn():
    with engine.connect() as conn:
        yield conn

