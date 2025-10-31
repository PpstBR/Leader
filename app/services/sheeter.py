from openpyxl import Workbook
from datetime import datetime
from io import BytesIO

# Função 1: salvar arquivo Excel localmente
def save_sheet(data: list[dict], filename: str | None = None) -> str:
    """Salva os resultados em um arquivo Excel local."""
    if not filename:
        filename = f"export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"

    wb = Workbook()
    ws = wb.active
    ws.title = "Resultados"

    if not data:
        ws.append(["Sem dados"])
    else:
        # Cabeçalhos
        ws.append(list(data[0].keys()))
        # Linhas
        for row in data:
            ws.append(list(row.values()))

    # Cria pasta exports se não existir
    import os
    os.makedirs("exports", exist_ok=True)
    file_path = f"exports/{filename}"
    wb.save(file_path)
    return file_path


# Função 2: gerar Excel e retornar como bytes (para download)
def generate_sheet_bytes(data: list[dict]) -> BytesIO:
    """Gera o arquivo Excel e o mantém em memória (para download HTTP)."""
    wb = Workbook()
    ws = wb.active
    ws.title = "Resultados"

    if not data:
        ws.append(["Sem dados"])
    else:
        ws.append(list(data[0].keys()))
        for row in data:
            ws.append(list(row.values()))

    buffer = BytesIO()
    wb.save(buffer)
    buffer.seek(0)
    return buffer
