"""
Módulo de criação da aplicação Flask.

Este módulo é responsável por criar e configurar a aplicação Flask,
incluindo a inicialização do log, adiciona error handles, 
registro de blueprints e configuração do log de requisições e respostas.

Funções:
    create_app: Cria e configura a aplicação Flask.

Variáveis:
    limiter: Instância do limitador de requisições.

Notas:
    Este módulo deve ser importado para ser chamado como ponto de entrada da aplicação.
"""

from flask import Flask, request, Response
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from apscheduler.schedulers.background import BackgroundScheduler

from app.config.logger_config import setup_logger
from app.functions import saiphwalker_caller

limiter = Limiter(get_remote_address, storage_uri="memory://")

def create_app() -> Flask:
    """
    Cria e configura a aplicação Flask.

    Esta função inicializa a aplicação Flask, configura o log, adiciona tratadores de erro,
    registra os blueprints e configura o log de requisições e respostas.

    Retorna:
        app (Flask)
    """

    # Cria a instância principal da aplicação Flask
    app = Flask(__name__)

    # Inicializa o limitador de requisições
    limiter.init_app(app)

    # Configura o log da aplicação
    setup_logger(app)

    # Inicializa o scheduler para v1 comente o comando abaixo
    # scheduler = BackgroundScheduler()
    # scheduler.add_job(saiphwalker_caller.execute, 'interval', minutes=5)
    # scheduler.start()

    @app.before_request
    def log_request_info() -> None:
        """
        Registra informações da requisição antes do processamento.

        Registra o método HTTP, caminho, cabeçalhos e corpo JSON das requisições recebidas.
        """

        # Tenta obter o corpo da requisição como JSON (retorna None se falhar ou não for JSON)
        data = request.get_json(silent=True)

        # Registra as informações da requisição
        app.logger.info(
            '[REQUEST] %s %s | Headers: %s | Body: %s',
            request.method,
            request.path,
            dict(request.headers),
            data if data else "No body or not JSON"
        )


    @app.after_request
    def log_response_info(response: Response) -> Response:
        """
        Registra informações da resposta após o processamento da requisição.

        Registra o status HTTP e o corpo das respostas. Trata erros durante o registro.

        Retorna:
            response (Response)

        Retorna:
            response (Response)
        """

        try:
            # Obtém o corpo da resposta como texto e registra o status e o corpo da resposta
            body = response.get_data(as_text=True)
            app.logger.info('[RESPONSE] %s | Body: %s', response.status, body)

        except AttributeError as e:
            # Registra erro caso ocorra uma exceção ao tentar logar a resposta
            app.logger.error('Erro ao logar resposta: %s', e)

        return response

    from app.handler.error_handlers import error_handlers # pylint: disable=import-outside-toplevel
    # Configura os tratadores de erro
    error_handlers(app)

    from app.routes.v1 import blueprints_v1 # pylint: disable=import-outside-toplevel
    from app.routes.v2 import blueprints_v2 # pylint: disable=import-outside-toplevel

    # Registra os blueprints das rotas
    for bp in blueprints_v1:
        app.register_blueprint(bp)

    for bp in blueprints_v2:
        app.register_blueprint(bp)

    return app
