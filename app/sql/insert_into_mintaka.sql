INSERT INTO mintaka 
    (
            id
        ,   name
        ,   symbol
        ,   current_price
        ,   market_cap
        ,   market_cap_rank
        ,   total_volume
        ,   high_24h
        ,   low_24h
        ,   price_change_24h
        ,   price_change_percentage_24h
        ,   price_change_percentage_24h_in_currency
        ,   price_change_percentage_7d_in_currency
        ,   price_change_percentage_30d_in_currency
        ,   market_cap_change_24h
        ,   market_cap_change_percentage_24h
        ,   ath
        ,   ath_change_percentage
        ,   ath_date
        ,   atl
        ,   atl_change_percentage
        ,   atl_date
        ,   circulating_supply
        ,   total_supply
        ,   max_supply
        ,   fully_diluted_valuation
        ,   last_updated
        ,   last_updated_at
        ,   image
        ,   usd
        ,   usd_24h_change
        ,   usd_24h_vol
        ,   usd_market_cap
    )
    
VALUES 
    (
            %s
        ,   %s
        ,   %s
        ,   %s
        ,   %s
        ,   %s
        ,   %s
        ,   %s
        ,   %s
        ,   %s
        ,   %s
        ,   %s
        ,   %s
        ,   %s
        ,   %s
        ,   %s
        ,   %s
        ,   %s
        ,   %s
        ,   %s
        ,   %s
        ,   %s
        ,   %s
        ,   %s
        ,   %s
        ,   %s
        ,   %s
        ,   %s
        ,   %s
        ,   %s
        ,   %s
        ,   %s
        ,   %s
    )
ON CONFLICT (id) 
DO UPDATE SET 
            name = EXCLUDED.name
        ,   symbol = EXCLUDED.symbol
        ,   current_price = EXCLUDED.current_price
        ,   market_cap = EXCLUDED.market_cap
        ,   market_cap_rank = EXCLUDED.market_cap_rank
        ,   total_volume = EXCLUDED.total_volume
        ,   high_24h = EXCLUDED.high_24h
        ,   low_24h = EXCLUDED.low_24h
        ,   price_change_24h = EXCLUDED.price_change_24h
        ,   price_change_percentage_24h = EXCLUDED.price_change_percentage_24h
        ,   price_change_percentage_24h_in_currency = EXCLUDED.price_change_percentage_24h_in_currency
        ,   price_change_percentage_7d_in_currency = EXCLUDED.price_change_percentage_7d_in_currency
        ,   price_change_percentage_30d_in_currency = EXCLUDED.price_change_percentage_30d_in_currency
        ,   market_cap_change_24h = EXCLUDED.market_cap_change_24h
        ,   market_cap_change_percentage_24h = EXCLUDED.market_cap_change_percentage_24h
        ,   ath = EXCLUDED.ath
        ,   ath_change_percentage = EXCLUDED.ath_change_percentage
        ,   ath_date = EXCLUDED.ath_date
        ,   atl = EXCLUDED.atl
        ,   atl_change_percentage = EXCLUDED.atl_change_percentage
        ,   atl_date = EXCLUDED.atl_date
        ,   circulating_supply = EXCLUDED.circulating_supply
        ,   total_supply = EXCLUDED.total_supply
        ,   max_supply = EXCLUDED.max_supply
        ,   fully_diluted_valuation = EXCLUDED.fully_diluted_valuation
        ,   last_updated = EXCLUDED.last_updated
        ,   last_updated_at = EXCLUDED.last_updated_at
        ,   image = EXCLUDED.image
        ,   usd = EXCLUDED.usd
        ,   usd_24h_change = EXCLUDED.usd_24h_change
        ,   usd_24h_vol = EXCLUDED.usd_24h_vol
        ,   usd_market_cap = EXCLUDED.usd_market_cap;