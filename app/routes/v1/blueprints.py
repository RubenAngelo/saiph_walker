from flask import Blueprint

bp_cripto = Blueprint('saiphwalker_cripto_api_v1', __name__, url_prefix='/api/saiphwalker/v1/cripto')
bp_health = Blueprint('saiphwalker_health_api_v1', __name__, url_prefix='/api/saiphwalker/v1/health')