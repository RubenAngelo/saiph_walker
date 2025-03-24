"""
Módulo de tratamento de erros do aplicativo Flask.

Este módulo é responsável por configurar os handlers de erro do aplicativo Flask,
lidando com erros como:

    Bad Request
    Unauthorized
    Forbidden
    Not Found
    Request Timeout
    Too Many Requests
    Internal Server Error
    Service Unavailable
    Gateway Timeout

Ele fornece uma função error_handlers que pode ser usada para configurar os
handlers de erro do aplicativo Flask.

Funções:
    error_handlers: Configura os handlers de erro do aplicativo Flask.

Notas:
    Este módulo utiliza a biblioteca Flask para configurar os handlers de erro.
"""

from typing import Dict, Tuple
import traceback

from flask import Flask
from app.util.utils import make_error_response

def error_handlers(app: Flask) -> None:
    """
    Função que configura os handlers de erro do aplicativo Flask.

    Os handlers de erro são funções que são chamadas quando o aplicativo
    Flask não consegue lidar com uma requisição. 

    Elas são responsáveis por lidar com erros como:

    Bad Request
    Unauthorized
    Forbidden
    Not Found
    Request Timeout
    Too Many Requests
    Internal Server Error
    Service Unavailable
    Gateway Timeout

    Retorna:
        app (Flask)
    """

    @app.errorhandler(400)
    def bad_request(error) -> Tuple[Dict, int]:
        """
        Handler do erro 400.

        Este handler é responsável por lidar com erros de Bad Request.
        """

        # Registra o erro no log
        app.logger.error(f'Erro: {error}')

        # Configura a resposta de erro retornada no response
        return make_error_response('Bad Request', error.description, 400)

    @app.errorhandler(401)
    def unauthorized(error) -> Tuple[Dict, int]:
        """
        Handler do erro 401.

        Este handler é responsável por lidar com erros de Unauthorized.
        """

        # Registra o erro no log
        app.logger.error(f'Erro: {error}')

        # Configura a resposta de erro retornada no response
        return make_error_response('Unauthorized', error.description, 401)

    @app.errorhandler(403)
    def forbidden(error) -> Tuple[Dict, int]:
        """
        Handler do erro 403.

        Este handler é responsável por lidar com erros de Forbidden.
        """
        # Registra o erro no log
        app.logger.error(f'Erro: {error}')

        # Configura a resposta de erro retornada no response
        return make_error_response('Forbidden', error.description, 403)

    @app.errorhandler(404)
    def not_found(error) -> Tuple[Dict, int]:
        """
        Handler do erro 404.

        Este handler é responsável por lidar com erros de Not Found.
        """

        # Registra o erro no log
        app.logger.error(f'Erro: {error}')

        # Configura a resposta de erro retornada no response
        return make_error_response('Not Found', error.description, 404)

    @app.errorhandler(408)
    def request_timeout(error) -> Tuple[Dict, int]:
        """
        Handler do erro 408.

        Este handler é responsável por lidar com erros de Request Timeout.
        """

        # Registra o erro no log
        app.logger.error(f'Erro: {error}')

        # Configura a resposta de erro retornada no response
        return make_error_response('Request Timeout', error.description, 408)

    @app.errorhandler(429)
    def too_many_requests(error) -> Tuple[Dict, int]:
        """
        Handler do erro 429.

        Este handler é responsável por lidar com erros de Too Many Requests.
        """

        # Registra o erro no log
        app.logger.error(f'Erro: {error}')

        # Configura a resposta de erro retornada no response
        return make_error_response('Too Many Requests', error.description, 429)

    @app.errorhandler(500)
    def internal_server_error(error) -> Tuple[Dict, int]:
        """
        Handler do erro 500.

        Este handler é responsável por lidar com erros de Internal Server Error.
        """

        # Registra o erro no log
        app.logger.error(f'Erro: {error}')

        # Configura a resposta de erro retornada no response
        return make_error_response('Internal Server Error', error.description, 500)

    @app.errorhandler(503)
    def service_unavailable(error) -> Tuple[Dict, int]:
        """
        Handler do erro 503.

        Este handler é responsável por lidar com erros de Service Unavailable.
        """

        # Registra o erro no log
        app.logger.error(f'Erro: {error}')

        # Configura a resposta de erro retornada no response
        return make_error_response('Service Unavailable', error.description, 503)

    @app.errorhandler(504)
    def gateway_timeout(error) -> Tuple[Dict, int]:
        """
        Handler do erro 504.

        Este handler é responsável por lidar com erros de Gateway Timeout.
        """

        # Registra o erro no log
        app.logger.error(f'Erro: {error}')

        # Configura a resposta de erro retornada no response
        return make_error_response('Gateway Timeout', error.description, 504)

    @app.errorhandler(Exception)
    def handler_exception(error: Exception) -> Tuple[Dict, int]:
        """
        Handler do erro genérico.

        Este handler é responsável por lidar com erros genéricos e que não
        são tratados por nenhum outro handler.
        """

        # Registra o erro no log
        app.logger.error(f'Erro: {error}\n{traceback.format_exc()}')

        # Configura a resposta de erro retornada no response
        return make_error_response('Internal Server Error', str(error), 500)
