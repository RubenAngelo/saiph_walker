"""
Este modulo define os blueprints para a API.

Variáveis:
    bp_cripto (Blueprint): Blueprint criado para a API cripto
    bp_health (Blueprint): Blueprint criado para a API health

Notas:
    Este módulo cria os blueprints e define a prefixo de URL para cada end-point.
"""

from flask import Blueprint

bp_cripto = Blueprint(
    'saiphwalker_cripto_api_v1', __name__, url_prefix='/api/saiphwalker/v1/cripto'
)
bp_health = Blueprint(
    'saiphwalker_health_api_v1', __name__, url_prefix='/api/saiphwalker/v1/health'
)
