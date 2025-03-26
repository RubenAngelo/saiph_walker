"""
Carregador de Variáveis de Ambiente

Este módulo carrega variáveis de ambiente de um arquivo .env usando a biblioteca dotenv.

Ele importa a função load_dotenv e a usa para carregar as variáveis de ambiente.
As variáveis carregadas estão acessíveis usando a função os.getenv.

Variáveis:
    BASE_URL (str): A URL base da aplicação
    KEY (str): Uma chave secreta para a aplicação

Notas:
    Este módulo utiliza a biblioteca dotenv para criar as variáveis de ambiente
    e as define no módulo atual.
"""

import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
KEY = os.getenv("KEY")

NAME_DB = os.getenv("NAME_DB")
USER_DB = os.getenv("USER_DB")
PASSWORD_DB = os.getenv("PASSWORD_DB")
HOST_DB = os.getenv("HOST_DB")
PORT_DB = os.getenv("PORT_DB")
