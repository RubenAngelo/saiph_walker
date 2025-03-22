def execute(price_change_percentage_1h: str, price_change_percentage_24h: str, price_change_percentage_7d: str, price_change_percentage_14d: str, price_change_percentage_30d: str, price_change_percentage_200d: str, price_change_percentage_1y: str) -> list[str]:
    price_change_dict = {
        '1h': price_change_percentage_1h,
        '24h': price_change_percentage_24h,
        '7d': price_change_percentage_7d,
        '14d': price_change_percentage_14d,
        '30d': price_change_percentage_30d,
        '200d': price_change_percentage_200d,
        '1y': price_change_percentage_1y
    }

    return [key for key, value in price_change_dict.items() if value == 'true']
