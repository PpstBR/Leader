import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# cria engine (mantém conexão com o SQL Server)
engine = create_engine(DATABASE_URL)

def run_query(sql: str, params: dict = None):
    """Executa uma query SQL e retorna lista de dicionários"""
    with engine.connect() as conn:
        result = conn.execute(text(sql), params or {})
        rows = [dict(row._mapping) for row in result]
    return rows
