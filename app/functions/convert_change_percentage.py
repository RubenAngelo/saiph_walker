"""
Módulo de conversão para o valor da variável price_change_percentage

Este módulo fornece uma função para converter o valor de price_change_percentage_*
em diferentes períodos de tempo.

Funções:
    execute: Retorna uma lista de strings representando os períodos de tempo
    para os quais price_change_percentage deve ser incluída no response.

Notas:
    Este módulo é utilizado para personalizar a resposta da API de criptomoedas.
"""

from typing import List

def execute(
    price_change_percentage_1h: str,
    price_change_percentage_24h: str,
    price_change_percentage_7d: str,
    price_change_percentage_14d: str,
    price_change_percentage_30d: str,
    price_change_percentage_200d: str,
    price_change_percentage_1y: str,
) -> List[str]:

    """
    Retorne uma lista de strings representando os períodos de tempo para os quais 
    price_change_percentage deve ser incluída no response.
    
    Parâmetros:
        price_change_percentage_1h (str)
        price_change_percentage_24h (str)
        price_change_percentage_7d (str)
        price_change_percentage_14d (str)
        price_change_percentage_30d (str)
        price_change_percentage_200d (str)
        price_change_percentage_1y (str)

    Retorna:
        List[str]
    """

    # Cria um dicionário que associa períodos de tempo com as variáveis de price_change_percentage
    price_change_dict = {
        '1h': price_change_percentage_1h,
        '24h': price_change_percentage_24h,
        '7d': price_change_percentage_7d,
        '14d': price_change_percentage_14d,
        '30d': price_change_percentage_30d,
        '200d': price_change_percentage_200d,
        '1y': price_change_percentage_1y,
    }

    # Retorna uma lista com as chaves (períodos de tempo) cujo valor correspondente é 'true'
    return [key for key, value in price_change_dict.items() if value == 'true']
