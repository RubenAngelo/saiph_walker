"""
Módulo para obter preços de criptomoedas.

Este módulo fornece uma função para obter os preços de uma lista de criptomoedas.
A função execute realiza uma requisição à API de criptomoedas e retorna os dados do response.

Funções:
    execute: Executa uma requisição à API para obter os preços de uma lista de criptomoedas.

Notas:
    A função execute retorna uma tupla contendo a resposta da API e o código de status.
"""

from typing import List, Tuple, Dict

from app.util.utils import make_request

def execute(
    ids: List[str],
    include_market_cap: str,
    include_24hr_vol: str,
    include_24hr_change: str,
    include_last_updated_at: str,
    vs_currencies: str = "usd",
) -> Tuple[Dict, int]:
    """
    Executa uma requisição à API para obter os preços de uma lista de criptomoedas.

    Parâmetros:
        ids (List[str])
        include_market_cap (str)
        include_24hr_vol (str)
        include_24hr_change (str)
        include_last_updated_at (str)
        vs_currencies (str)

    Retorna:
        Tuple[dict, int]
    """

    # Junta a lista de price_change_percentage com virgula
    ids = "%2C".join(ids)

    # Faz a requisição para a API
    return make_request(
        f"/simple/price?ids={ids}&"
        f"vs_currencies={vs_currencies}&"
        f"include_market_cap={include_market_cap}&"
        f"include_24hr_vol={include_24hr_vol}&"
        f"include_24hr_change={include_24hr_change}&"
        f"include_last_updated_at={include_last_updated_at}"
    )
