from app.util.utils import make_error_response
import traceback

def error_handlers(app):
    @app.errorhandler(400)
    def bad_request(error):
        app.logger.error(f'Erro: {error}')
        return make_error_response('Bad Request', error.description, 400)

    @app.errorhandler(401)
    def unauthorized(error):
        app.logger.error(f'Erro: {error}')
        return make_error_response('Unauthorized', error.description, 401)

    @app.errorhandler(403)
    def forbidden(error):
        app.logger.error(f'Erro: {error}')
        return make_error_response('Forbidden', error.description, 403)

    @app.errorhandler(404)
    def not_found(error):
        app.logger.error(f'Erro: {error}')
        return make_error_response('Not Found', error.description, 404)

    @app.errorhandler(408)
    def request_timeout(error):
        app.logger.error(f'Erro: {error}')
        return make_error_response('Request Timeout', error.description, 408)

    @app.errorhandler(429)
    def too_many_requests(error):
        app.logger.error(f'Erro: {error}')
        return make_error_response('Too Many Requests', error.description, 429)

    @app.errorhandler(500)
    def internal_server_error(error):
        app.logger.error(f'Erro: {error}')
        return make_error_response('Internal Server Error', error.description, 500)

    @app.errorhandler(503)
    def service_unavailable(error):
        app.logger.error(f'Erro: {error}')
        return make_error_response('Service Unavailable', error.description, 503)

    @app.errorhandler(504)
    def gateway_timeout(error):
        app.logger.error(f'Erro: {error}')
        return make_error_response('Gateway Timeout', error.description, 504)

    @app.errorhandler(Exception)
    def handler_exception(error):
        app.logger.error(f'Erro: {error}\n{traceback.format_exc()}')
        return make_error_response('Internal Server Error', str(error), 500)
