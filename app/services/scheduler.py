from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from app.services.db import run_query
from app.utils.sql_loader import get_query
from app.services.sheeter import save_sheet

def nightly_export_job():
    """Executa uma exportação SQL automática toda noite."""
    print(f"[{datetime.now()}] Iniciando exportação automática...")
    try:
        date = datetime.now().strftime("%Y-%m-%d") 
        # Exemplo de query noturna fixa (pode ajustar o nome)
        sql = get_query("todas_pessoas")
        data = run_query(sql, {"limit": 10000})
        file_path = save_sheet(data, f"leads-{date}.xlsx")
        print(f"[{datetime.now()}] Exportação concluída: {file_path} ({len(data)} linhas)")
    except Exception as e:
        print(f"[{datetime.now()}] Erro na exportação automática: {e}")

def start_scheduler():
    """Inicializa o agendador de tarefas."""
    scheduler = BackgroundScheduler()
    # Agenda para rodar todo dia às 2h da manhã
    scheduler.add_job(nightly_export_job, "cron", hour=0, minute=10)
    scheduler.start()
    print("⏰ Agendador de exportação iniciado (diariamente às 00:10)")
