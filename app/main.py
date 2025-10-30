from fastapi import FastAPI
from app.routes import extractor

app = FastAPI(title="SQL Extractor API")

# inclui as rotas
app.include_router(extractor.router)

@app.get("/")
def root():
    return {"message": "SQL Extractor API is running 🚀"}