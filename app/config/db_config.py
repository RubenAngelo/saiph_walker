import psycopg2

from app.constant.constants import NAME_DB, USER_DB, PASSWORD_DB, HOST_DB, PORT_DB

def connect_to_db():
    # Configuração da conexão
    conn = psycopg2.connect(
        dbname=NAME_DB,
        user=USER_DB,
        password=PASSWORD_DB,
        host=HOST_DB,
        port=PORT_DB
    )

    return conn
