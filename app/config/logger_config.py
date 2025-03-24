"""
Módulo de configuração de logger para o aplicativo Flask.

Este módulo fornece uma função para configurar um logger para o aplicativo Flask,
incluindo a criação de um diretório de logs, um arquivo de log com data e hora,
e a configuração de handlers para arquivo e console.

Funções:
    setup_logger(app): Configura um logger para o aplicativo Flask fornecido.

Notas:
    Este módulo utiliza a biblioteca logging do Python para configurar o logger.
    A função setup_logger deve ser chamada após a criação do aplicativo Flask.
"""
import os
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
from flask import Flask

def setup_logger(app: Flask) -> None:
    """
    Configura um logger para o aplicativo Flask fornecido.

    Esta função configura os handlers de log tanto para arquivo quanto para console,
    utilizando um handler file para gerenciar os arquivos de log.

    Parâmetros:
        app (Flask)
    """

    # Define o caminho do diretório de logs
    log_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '..', '..', 'logs'
    )
    os.makedirs(log_dir, exist_ok=True)  # Cria o diretório de logs se ele não existir

    # Gera um nome de arquivo de log com data e hora
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M')
    log_file = os.path.join(log_dir, f'app_{timestamp}.log')

    # Configura um file handler para o arquivo de log
    file_handler = RotatingFileHandler(
        log_file, maxBytes=1_000_000, backupCount=5, encoding='utf-8'
    )
    file_handler.setLevel(logging.INFO)  # Define o nível de log como INFO para o file handler

    # Define o formato das mensagens de log
    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)s | %(name)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    file_handler.setFormatter(formatter)  # Aplica o formato ao file handler

    # Adiciona o file handler ao logger do app
    app.logger.setLevel(logging.INFO)  # Define o nível de log como INFO para o logger do app
    app.logger.addHandler(file_handler)

    # Configura um handler para exibir logs no console
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)  # Aplica o formato ao manipulador de console
    app.logger.addHandler(console_handler)
