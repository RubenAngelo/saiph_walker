import requests
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
KEY = os.getenv("KEY")

def make_request(endpoint):
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
        print("Erro: A requisição excedeu o tempo limite.")
        return None, 504

    except requests.exceptions.HTTPError as http_err:
        print(f"Erro HTTP: {http_err}")

    except requests.exceptions.RequestException as req_err:
        print(f"Erro de requisição: {req_err}")

    return None, 503
