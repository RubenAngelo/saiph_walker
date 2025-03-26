"""
Módulo para lidar com requisições de saúde da API.

Este módulo fornece uma função para verificar o status da API, retornando um objeto JSON
com o status da API e sua versão.

Funções:
    health_check: /health/check End-point para verificar o status da API.

Notas:
    Este módulo utiliza a biblioteca Flask para criar o end-point
    e a biblioteca Flask-Limiter para limitar o número de requisições por minuto.
"""

from typing import Tuple
from flask import jsonify, Response

from app import limiter
from app.util.utils import current_timestamp
from app.routes.v2.blueprints import bp_health as bp

@bp.route('/check', methods=['GET'])
@limiter.limit("3 per minute")
def health_check() -> Tuple[Response, int]:
    """
    Retorna o status da API.

    Este endpoint é usado para verificar o status da API. Ele retorna um objeto JSON
    com o status da API e sua versão.

    Retorna:
        (Tuple[Response, int])
    """

    return jsonify(
        {
            'status': '(V2) To the Orion, my friend!',
            'status_code': 200,
            'timestamp': current_timestamp()
        }
    ), 200
