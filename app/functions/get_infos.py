"""
Módulo para obter informações de criptomoedas.

Este módulo fornece uma função para obter informações de uma lista de criptomoedas.
A função execute realiza uma requisição à API de criptomoedas e retorna os dados do response.

Funções:
    execute: Obtém as informações de uma lista de criptomoedas.

Notas:
    A função execute retorna uma tupla contendo os dados da resposta e o código de status.
"""

from typing import List, Tuple, Dict

from app.util.utils import make_request

def execute(
    order: str,
    per_page: str,
    price_change_percentage: List[str],
    vs_currency: str = "usd"
) -> Tuple[Dict, int]:
    """
    Obtém as informações de uma lista de criptomoedas.

    Parâmetros:
        order (str)
        per_page (str)
        price_change_percentage (List[str])
        vs_currency (str)

    Retorna:
        Tuple[dict, int]
    """

    # Junta a lista de price_change_percentage com virgula
    price_change_percentage = "%2C".join(price_change_percentage)

    # Obtém o número de criptomoedas por página
    per_page = per_page.split("_")[1]

    # Faz a requisição para a API
    return make_request(
        f"/coins/markets?vs_currency={vs_currency}&"
        f"order={order}&"
        f"per_page={per_page}&"
        f"price_change_percentage={price_change_percentage}"
    )
