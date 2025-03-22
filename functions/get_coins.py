from utils.utils import make_request

def get_coins(vs_currency: str, order: str, per_page: str, price_change_percentage: list[str]) -> tuple[dict, int]:
    price_change_percentage="%2C".join(price_change_percentage.split(","))
    return make_request(
        f"/coins/markets?vs_currency={vs_currency}&"
        f"order={order}&"
        f"per_page={per_page}&"
        f"price_change_percentage={price_change_percentage}"
    )
