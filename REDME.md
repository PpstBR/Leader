# SQL Extractor API (Python + FastAPI)

API para executar consultas SQL pré-definidas em um banco SQL Server.

## 🚀 Como rodar

```bash
python -m venv venv
source venv/bin/activate   # ou venv\Scripts\activate no Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
