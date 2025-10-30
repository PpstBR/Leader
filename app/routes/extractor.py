from fastapi import APIRouter, Query
from app.db import run_query
from app.utils.sql_loader import get_query

router = APIRouter(prefix="/extract", tags=["Extractor"])

@router.get("/")
def extract_data(query_name: str = Query(..., description="Nome da query a ser executada"),
                 limit: int = Query(100, description="Limite de registros")):
    sql = get_query(query_name)
    if not sql:
        return {"error": f"Query '{query_name}' não encontrada."}
    data = run_query(sql, {"limit": limit})
    return {"rows": data, "count": len(data)}
