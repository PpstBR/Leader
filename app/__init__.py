# app/__init__.py
"""
Pacote principal da aplicação FastAPI.
Aqui definimos o que deve ser importado quando se faz `import app`.
"""

from .services import db
from . import routes, utils
