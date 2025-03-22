from flask import Flask, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from app.functions.logger_config import setup_logger

limiter = Limiter(get_remote_address)

def create_app():
    app = Flask(__name__)

    limiter.init_app(app)

    setup_logger(app)

    @app.before_request
    def log_request_info():
        data = request.get_json(silent=True)
        app.logger.info(f'[REQUEST] {request.method} {request.path} | Headers: {dict(request.headers)} | Body: {data if data else "No body or not JSON"}')

    @app.after_request
    def log_response_info(response):
        try:
            body = response.get_data(as_text=True)
            app.logger.info(f'[RESPONSE] {response.status} | Body: {body}')
        except Exception as e:
            app.logger.error(f'Erro ao logar resposta: {e}')
        return response

    from app.handler.handlers import error_handlers
    error_handlers(app)

    from app.routes.v1 import blueprints_v1
    for bp in blueprints_v1:
        app.register_blueprint(bp)

    return app
