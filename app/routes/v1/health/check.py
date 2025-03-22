from flask import jsonify
from app.util.utils import current_timestamp
from app.routes.v1.blueprints import bp_health as bp

@bp.route('/check', methods=['GET'])
def health_check():
    return jsonify({'status': 'To the Orion my friend', 'status_code': 200, 'timestamp': current_timestamp()}), 200
