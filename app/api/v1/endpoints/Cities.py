from sqlalchemy.engine import Connection
from fastapi import APIRouter, Depends
from sqlalchemy import text
from app.config.databases import db_conn

router = APIRouter()

@router.get('/')
def get_cities(conn: Connection = Depends(db_conn)):
    query = """
        SELECT  Country,Continent
        FROM world_masters
        group by Continent,Country

    """
    result = conn.execute(text(query))
    return [dict(row._mapping) for row in result]

