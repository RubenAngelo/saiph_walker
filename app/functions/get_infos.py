from app.util.utils import make_request

def execute(order: str, per_page: str, price_change_percentage: list[str], vs_currency: str = "usd") -> tuple[dict, int]:
    price_change_percentage = "%2C".join(price_change_percentage)
    per_page = per_page.split("_")[1]

    return make_request(
        f"/coins/markets?vs_currency={vs_currency}&"
        f"order={order}&"
        f"per_page={per_page}&"
        f"price_change_percentage={price_change_percentage}"
    )
