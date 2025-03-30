"""
Módulo de configuração de conexão com o banco de dados PostgreSQL.
Este módulo fornece uma função para estabelecer uma conexão com o banco de dados
PostgreSQL utilizando os parâmetros de configuração definidos em constants.

Funções:
    - connect_to_db(): Estabelece e retorna uma conexão com o banco de dados.
    
Dependências:
    - psycopg2: Biblioteca para conexão com o banco de dados PostgreSQL.
    - app.constant.constants: Módulo que contém as constantes de configuração
    do banco de dados, como NAME_DB, USER_DB, PASSWORD_DB, HOST_DB e PORT_DB.
"""

import psycopg2

from app.constant.constants import NAME_DB, USER_DB, PASSWORD_DB, HOST_DB, PORT_DB

def connect_to_db():
    """
    Estabelece uma conexão com o banco de dados PostgreSQL usando os parâmetros
    de configuração fornecidos.
    Retorna:
        psycopg2.extensions.connection: Um objeto de conexão para interagir com o banco de dados.
    """
    # Configuração da conexão
    conn = psycopg2.connect(
        dbname=NAME_DB,
        user=USER_DB,
        password=PASSWORD_DB,
        host=HOST_DB,
        port=PORT_DB
    )

    return conn
