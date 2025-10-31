from fastapi import APIRouter, Query
from fastapi.responses import StreamingResponse
from app.services.db import run_query
from app.utils.sql_loader import get_query
from app.services.sheeter import save_sheet, generate_sheet_bytes

router = APIRouter(prefix="/sheets", tags=["extractor"])


@router.get("/download")
def extract_and_download(query_name: str = Query(...), limit: int = 100):
    """Executa a query e retorna o Excel para download."""
    sql = get_query(query_name)
    data = run_query(sql, {"limit": limit})
    excel_bytes = generate_sheet_bytes(data)

    filename = f"{query_name}_{limit}.xlsx"
    headers = {"Content-Disposition": f"attachment; filename={filename}"}
    return StreamingResponse(excel_bytes, media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", headers=headers)
