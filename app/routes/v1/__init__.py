"""
Este modulo insere os blueprints para a API em uma lista.

Variáveis:
    blueprints_v1 (list): Captura os blueprints da API

Notas:
    Este módulo utiliza os blueprints criados em outros módulos.
"""

from app.routes.v1.cripto.info_price import bp as cripto_bp
from app.routes.v1.health.check import bp as health_bp

blueprints_v1 = [cripto_bp, health_bp]
