def execute(infos: dict, prices: dict) -> dict:
    for info in infos:
        price_values = prices.get(info["id"])
        if price_values:
            info.update(price_values)

    return infos
