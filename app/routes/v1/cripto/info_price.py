from flask import jsonify, request, abort
from pydantic import ValidationError

from app import limiter
from app.functions import get_infos, get_prices, convert_change_percentage, headers_validator
from app.util.utils import unpack
from app.routes.v1.blueprints import bp_cripto as bp

@bp.route('/info/price/execute', methods=['GET'])
@limiter.limit("3 per minute")
def get_infos_prices():
    try:
        order,\
        per_page,\
        include_market_cap,\
        include_24hr_vol,\
        include_24hr_change,\
        include_last_updated_at,\
        price_change_percentage_1h,\
        price_change_percentage_24h,\
        price_change_percentage_7d,\
        price_change_percentage_14d,\
        price_change_percentage_30d,\
        price_change_percentage_200d,\
        price_change_percentage_1y = unpack(headers_validator.execute.join_info_price_headers(request.headers))

    except ValidationError as e:
        abort(400, description=f"Malformed headers: {str(e)}")

    price_change_percentage = convert_change_percentage.execute(
        price_change_percentage_1h=price_change_percentage_1h,
        price_change_percentage_24h=price_change_percentage_24h,
        price_change_percentage_7d=price_change_percentage_7d,
        price_change_percentage_14d=price_change_percentage_14d,
        price_change_percentage_30d=price_change_percentage_30d,
        price_change_percentage_200d=price_change_percentage_200d,
        price_change_percentage_1y=price_change_percentage_1y
    )

    infos, status = get_infos.execute(
        order=order,
        per_page=per_page,
        price_change_percentage=price_change_percentage
    )

    if status != 200:
        abort(status, description=infos.get('error', infos.get('status', {}).get('error_message', 'Unknown error')))

    prices, status = get_prices.execute(
        ids=[coin["id"] for coin in infos],
        include_market_cap=include_market_cap,
        include_24hr_vol=include_24hr_vol,
        include_24hr_change=include_24hr_change,
        include_last_updated_at=include_last_updated_at
    )

    if status != 200:
        abort(status, description=prices.get('error', prices.get('status', {}).get('error_message', 'Unknown error')))

    for info in infos:
        price_values = prices.get(info["id"])
        if price_values:
            info.update(price_values)

    return jsonify(infos), 200
