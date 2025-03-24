"""
Módulo de utilidades para a API.

Este módulo fornece funções auxiliares para realizar requisições à API CoinGecko,
tratar erros e formatar respostas.

Funções:
    make_request: Faz uma requisição GET à API CoinGecko.
    make_error_response: Cria uma resposta de erro com o nome do erro, descrição e código de status.
    current_timestamp: Retorna o timestamp atual em segundos.

Notas:
    Este módulo utiliza a biblioteca Flask para criar respostas JSON
    e a biblioteca requests para realizar requisições à API CoinGecko.
"""

from datetime import datetime
from typing import Tuple, Dict

from flask import jsonify
import requests

from app.constant.constants import BASE_URL, KEY

def make_request(endpoint: str) -> Tuple[Dict, int]:
    """
    Faz uma requisição GET à API CoinGecko.

    Parâmetros:
        endpoint (str)

    Retorna:
        Tuple[Dict, int]
    """

    headers = {
        "accept": "application/json",
        "x-api-key": KEY
    }

    try:
        # Realiza a requisição GET com um timeout de 10 segundos
        response = requests.get(
            f"{BASE_URL}{endpoint}",
            headers=headers,
            timeout=10
        )

        # Retorna o conteúdo JSON da resposta e o código de status
        return response.json(), response.status_code

    except requests.exceptions.Timeout:
        # Retorna um erro 504 se a requisição exceder o tempo limite
        return {"error": "Timeout from CoinGecko API"}, 504

    except requests.exceptions.HTTPError as http_err:
        # Retorna um erro 503 para problemas HTTP específicos
        return {"error": f"Error HTTP from CoinGecko API: {http_err}"}, 503

    except requests.exceptions.RequestException as req_err:
        # Retorna um erro 503 para qualquer problema na requisição
        return {"error": f"Error from CoinGecko API: {req_err}"}, 503

def current_timestamp() -> float:
    """
    Retorna o timestamp atual em segundos.

    Retorna:
        float
    """

    return datetime.utcnow().timestamp()

def make_error_response(
    error_name: str, description: str, status_code: int
) -> Tuple[Dict, int]:
    """
    Cria uma resposta de erro com o nome do erro, descrição e código de status.
    Retorna uma tupla com o conteúdo da resposta e o código de status.

    Args:
        error_name (str)
        description (str)
        status_code (int)

    Retorna:
        tuple[dict, int]
    """

    return jsonify({
        'error': error_name,
        'description': description,
        'status_code': status_code,
        'timestamp': current_timestamp()
    }), status_code
