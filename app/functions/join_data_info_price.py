"""
Módulo para mesclar dados de preço com informações de criptomoedas.

Este módulo fornece uma função para combinar dados de preço com informações sobre criptomoedas.
A função execute realiza a mescla dos dados e retorna um dicionário com as informações atualizadas.

Funções:
    execute: Mescla os dados de preço com as informações de criptomoedas.

Notas:
    A função execute espera dois dicionários como entrada: infos e prices
    O dicionário infos deve conter informações sobre as criptomoedas,
    enquanto o dicionário prices deve conter dados de preço para as criptomoedas.

    A função retorna um dicionário com as informações das criptomoedas atualizadas,
    incluindo os dados de preço.
"""

from typing import Dict, List

def execute(
    infos: List[Dict[str, str]],
    prices: Dict[str, Dict[str, str]]
) -> List[Dict[str, str]]:
    """
    Mescla os dados de preço nas informações correspondentes da criptomoeda.

    Parâmetros:
        infos (List[Dict[str, str]])
        prices (Dict[str, Dict[str, str]])

    Retorna:
        infos (List[Dict[str, str]])
    """

    for info in infos:
        # Recupera os dados de preço para a criptomoeda atual pelo seu ID
        price_values = prices.get(info["id"])
        if price_values:
            # Atualiza as informações da criptomoeda com os dados de preço
            info.update(price_values)

    return infos
