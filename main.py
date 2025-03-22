from functions.get_coins import get_coins
from functions.get_prices import get_prices

from flask import Flask, jsonify, abort, request
from datetime import datetime

app = Flask(__name__)

@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad Request', 'description': error.description, 'status_code': 400, 'timestamp': datetime.now().timestamp()}), 400

@app.errorhandler(401)
def unauthorized(error):
    return jsonify({'error': 'Unauthorized', 'description': error.description, 'status_code': 401, 'timestamp': datetime.now().timestamp()}), 401

@app.errorhandler(403)
def forbidden(error):
    return jsonify({'error': 'Forbidden', 'description': error.description, 'status_code': 403, 'timestamp': datetime.now().timestamp()}), 403

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not Found', 'description': error.description, 'status_code': 404, 'timestamp': datetime.now().timestamp()}), 404

@app.errorhandler(408)
def request_timeout(error):
    return jsonify({'error': 'Request Timeout', 'description': error.description, 'status_code': 408, 'timestamp': datetime.now().timestamp()}), 408

@app.errorhandler(429)
def too_many_requests(error):
    return jsonify({'error': 'Too Many Requests', 'description': error.description, 'status_code': 429, 'timestamp': datetime.now().timestamp()}), 429

@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error': 'Internal Server Error', 'description': error.description, 'status_code': 500, 'timestamp': datetime.now().timestamp()}), 500

@app.errorhandler(503)
def service_unavailable(error):
    return jsonify({'error': 'Service Unavailable', 'description': error.description, 'status_code': 503, 'timestamp': datetime.now().timestamp()}), 503

@app.errorhandler(504)
def gateway_timeout(error):
    return jsonify({'error': 'Gateway Timeout', 'description': error.description, 'status_code': 504, 'timestamp': datetime.now().timestamp()}), 504

@app.errorhandler(Exception)
def handler_exception(error):
    return jsonify({'error': 'Internal Server Error', 'description': "Exception", 'status_code': 500, 'timestamp': datetime.now().timestamp()}), 500

@app.route('api/saiphwalker/v1/joindata/execute', methods=['GET'])
def _execute()-> tuple[dict, int]:
    headers = dict(request.headers)

    coins, status = get_coins(
        vs_currency=headers['Vs-Currency'] if 'Vs-Currency' in headers else 'usd',
        order=headers['Order'] if 'Order' in headers else 'market_cap_desc',
        per_page=headers['Per-Page'] if 'Per-Page' in headers else '5',
        price_change_percentage=headers['Price-Change-Percentage'] if 'Price-Change-Percentage' in headers else '24h,7d,30d'
    )

    if status != 200:
        abort(status, description=coins['error'] if 'error' in coins else coins['status']['error_message'])
        return

    prices, status = get_prices(
        ids=[coin["id"] for coin in coins],
        vs_currencies=headers['Vs-Currency'] if 'Vs-Currency' in headers else 'usd',
        include_market_cap=headers['Include-Market-Cap'] if 'Include-Market-Cap' in headers else 'true',
        include_24hr_vol=headers['Include-24Hr-Vol'] if 'Include-24Hr-Vol' in headers else 'true',
        include_24hr_change=headers['Include-24Hr-Change'] if 'Include-24Hr-Change' in headers else 'true',
        include_last_updated_at=headers['Include-Last-Updated-At'] if 'Include-Last-Updated-At' in headers else 'true'
    )

    if status != 200:
        abort(status, description=prices['error'] if 'error' in prices else prices['status']['error_message'])
        return

    for coin in coins:
        price_values = prices.get(coin["id"])
        if price_values:
            coin.update(price_values)

    return jsonify(coins), 200

if __name__ == '__main__':
    app.run(debug=True)
