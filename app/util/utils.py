from datetime import datetime

from app.constant.constants import BASE_URL, KEY

from flask import jsonify
import requests

def make_request(endpoint: str) -> tuple[dict, int]:
    headers = {
        "accept": "application/json",
        "x-api-key": KEY
    }

    try:
        response = requests.get(
            f"{BASE_URL}{endpoint}",
            headers=headers,
            timeout=10
        )

        return response.json(), response.status_code

    except requests.exceptions.Timeout:
        return {"error": "Timeout from CoinGecko API"}, 504

    except requests.exceptions.HTTPError as http_err:
        return {"error": f"Error from CoinGecko API: {http_err}"}, 503

    except requests.exceptions.RequestException as req_err:
        return {"error": f"Error from CoinGecko API: {req_err}"}, 503

def current_timestamp() -> float:
    return datetime.utcnow().timestamp()

def unpack(headers: dict[str, str]) -> list[str]:
    return [value for key, value in headers]

def make_error_response(error_name: str, description: str, status_code: int) -> tuple[dict, int]:
    return jsonify({
        'error': error_name,
        'description': description,
        'status_code': status_code,
        'timestamp': current_timestamp()
    }), status_code
