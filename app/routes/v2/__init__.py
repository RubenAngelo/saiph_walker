"""
Este modulo insere os blueprints para a API em uma lista.

Variáveis:
    blueprints_v2 (list): Captura os blueprints da API

Notas:
    Este módulo utiliza os blueprints criados em outros módulos.
"""

from app.routes.v2.cripto.info_price import bp as cripto_bp
from app.routes.v2.health.check import bp as health_bp

blueprints_v2 = [cripto_bp, health_bp]
