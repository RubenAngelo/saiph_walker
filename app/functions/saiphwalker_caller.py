"""
Este módulo define uma função para executar uma requisição POST a um endpoint específico da API.
Funções:
    execute():
        Envia uma requisição POST para a API SaiphWalker para executar uma operação específica.
        Se a requisição falhar devido a uma RequestException, a função espera 15 segundos
        e tenta novamente de forma recursiva.
Exceções:
    requests.exceptions.RequestException: Caso a requisição falhe após as tentativas.
"""

import time

import requests

from app.constant.constants import HOST_SAIPHWALKER

def execute():
    """
    Envia uma requisição POST para a API SaiphWalker para executar uma operação
    de informação de preço.
    Caso a requisição falhe devido a uma RequestException, a função espera 15 segundos
    e tenta novamente de forma recursiva.

    Observação:
        - Certifique-se de que a variável HOST_SAIPHWALKER esteja devidamente definida e acessível.
        - Chamadas recursivas podem levar a um estouro de pilha se o problema 
        persistir indefinidamente.

    Exceções:
        requests.exceptions.RequestException: Caso a requisição falhe e a recursão
        não seja tratada adequadamente.
    """

    try:
        requests.post(f"{HOST_SAIPHWALKER}/api/saiphwalker/v2/cripto/info/price/execute", timeout=10)

    except requests.exceptions.RequestException:
        time.sleep(15)
        execute()
