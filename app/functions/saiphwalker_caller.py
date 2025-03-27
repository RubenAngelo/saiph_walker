import requests
import time
from app.constant.constants import HOST_SAIPHWALKER

def execute():
    try:
        requests.post(f"{HOST_SAIPHWALKER}/api/saiphwalker/v2/cripto/info/price/execute", timeout=10)
    except Exception:
        time.sleep(15)
        execute()
