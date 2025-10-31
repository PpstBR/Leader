# app/routes/__init__.py
"""
Módulo de rotas da aplicação.
Aqui podemos importar automaticamente os roteadores disponíveis.
"""

from .router import router as extractor_router

# Lista de todos os routers disponíveis (para incluir no main.py)
__all__ = ["extractor_router"]
