from utils.utils import make_request

def get_prices(ids: list[str], vs_currencies: str, include_market_cap: str, include_24hr_vol: str, include_24hr_change: str, include_last_updated_at: str) -> tuple[dict, int]:
    ids = ",".join(ids)
    return make_request(
        f"/simple/price?ids={ids}&"
        f"vs_currencies={vs_currencies}&"
        f"include_market_cap={include_market_cap}&"
        f"include_24hr_vol={include_24hr_vol}&"
        f"include_24hr_change={include_24hr_change}&"
        f"include_last_updated_at={include_last_updated_at}"
    )
