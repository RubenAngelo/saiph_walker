"""
Constants:
-----------
- HOST_SAIPHWALKER : str
    O endereço do host para a aplicação SaiphWalker, carregado da variável de ambiente HOST_SAIPHWALKER.

- BASE_URL : str
    A URL base para a aplicação, carregada da variável de ambiente BASE_URL.
    
- KEY : str
    A chave ou segredo da API, carregado da variável de ambiente KEY.
- NAME_DB : str
    O nome do banco de dados, carregado da variável de ambiente NAME_DB.
- USER_DB : str
    O nome de usuário para a conexão com o banco de dados, carregado da variável de ambiente USER_DB.
- PASSWORD_DB : str
    A senha para a conexão com o banco de dados, carregada da variável de ambiente PASSWORD_DB.
- HOST_DB : str
    O endereço do host para o banco de dados, carregado da variável de ambiente HOST_DB.
- PORT_DB : str
    O número da porta para a conexão com o banco de dados, carregado da variável de ambiente PORT_DB.

Dependências:
-------------
- os : Módulo da biblioteca padrão para interagir com o sistema operacional.
- dotenv : Biblioteca de terceiros para carregar variáveis de ambiente de um arquivo .env.

Nota:
-----
Certifique-se de que um arquivo .env com as variáveis necessárias esteja presente no diretório raiz
da aplicação ou que as variáveis de ambiente estejam configuradas no sistema antes de executar a aplicação.
"""

import os

from dotenv import load_dotenv

load_dotenv()

HOST_SAIPHWALKER = os.getenv("HOST_SAIPHWALKER")

BASE_URL = os.getenv("BASE_URL")
KEY = os.getenv("KEY")

NAME_DB = os.getenv("NAME_DB")
USER_DB = os.getenv("USER_DB")
PASSWORD_DB = os.getenv("PASSWORD_DB")
HOST_DB = os.getenv("HOST_DB")
PORT_DB = os.getenv("PORT_DB")
