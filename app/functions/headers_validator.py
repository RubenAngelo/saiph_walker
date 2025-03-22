from pydantic import BaseModel, constr

class execute(BaseModel):
    order: constr(pattern='^(market_cap_desc|market_cap_asc|volume_asc|volume_desc|id_asc|id_desc)$') = 'market_cap_desc'
    per_page: constr(pattern='^(top_1|top_2|top_3|top_4|top_5|top_6|top_7|top_8|top_9|top_10)$') = 'top_5'
    include_market_cap: constr(pattern='^(true|false)$') = 'true'
    include_24hr_vol: constr(pattern='^(true|false)$') = 'true'
    include_24hr_change: constr(pattern='^(true|false)$') = 'true'
    include_last_updated_at: constr(pattern='^(true|false)$') = 'true'
    price_change_percentage_1h: constr(pattern='^(true|false)$') = 'false'
    price_change_percentage_24h: constr(pattern='^(true|false)$') = 'true'
    price_change_percentage_7d: constr(pattern='^(true|false)$') = 'true'
    price_change_percentage_14d: constr(pattern='^(true|false)$') = 'false'
    price_change_percentage_30d: constr(pattern='^(true|false)$') = 'true'
    price_change_percentage_200d: constr(pattern='^(true|false)$') = 'false'
    price_change_percentage_1y: constr(pattern='^(true|false)$') = 'false'

    @classmethod
    def join_info_price_headers(cls, headers: dict[str, str]) -> classmethod:
        data = {
            'order': headers.get('Order', 'market_cap_desc').lower(),
            'per_page': headers.get('Per-Page', 'top_5').lower(),
            'include_market_cap': headers.get('Include-Market-Cap', 'true').lower(),
            'include_24hr_vol': headers.get('Include-24Hr-Vol', 'true').lower(),
            'include_24hr_change': headers.get('Include-24Hr-Change', 'true').lower(),
            'include_last_updated_at': headers.get('Include-Last-Updated-At', 'true').lower(),
            'price_change_percentage_1h': headers.get('Price-Change-Percentage-1H', 'false').lower(),
            'price_change_percentage_24h': headers.get('Price-Change-Percentage-24H', 'true').lower(),
            'price_change_percentage_7d': headers.get('Price-Change-Percentage-7D', 'true').lower(),
            'price_change_percentage_14d': headers.get('Price-Change-Percentage-14D', 'false').lower(),
            'price_change_percentage_30d': headers.get('Price-Change-Percentage-30D', 'true').lower(),
            'price_change_percentage_200d': headers.get('Price-Change-Percentage-200D', 'false').lower(),
            'price_change_percentage_1y': headers.get('Price-Change-Percentage-1Y', 'false').lower()
        }

        return cls(**data)
