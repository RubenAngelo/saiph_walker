"""
Módulo para lidar com requisições de informações e preços de criptomoedas.

Este módulo fornece uma função para obter informações e preços de criptomoedas,
utilizando a API pública da CoinGecko. Ele também inclui funcionalidades para
validar headers HTTP e converter valores de price_change_percentage.

Funções:
    get_infos_prices: /cripto/info/price/execute End-point para obter informações e preços de criptomoedas.

Notas:
    Este módulo utiliza a biblioteca Flask para criar o end-point
    e a biblioteca Pydantic para validar os headers HTTP.
"""

from typing import Tuple

from pydantic import ValidationError

from flask import jsonify, request, abort, Response

from app import limiter
from app.functions import (
    get_infos,
    get_prices,
    convert_change_percentage,
    headers_validator,
    join_data_info_price
)

from app.routes.v1.blueprints import bp_cripto as bp

@bp.route('/info/price/execute', methods=['GET'])
@limiter.limit("3 per minute")
def get_infos_prices() -> Tuple[Response, int]:
    """
    End-point para obter informações e preços de criptomoedas.

    Os parâmetros são: 

    order
    per_page
    include_market_cap
    include_24hr_vol
    include_24hr_change
    include_last_updated_at
    price_change_percentage_1h
    price_change_percentage_24h
    price_change_percentage_7d
    price_change_percentage_14d
    price_change_percentage_30d
    price_change_percentage_200d
    price_change_percentage_1y

    O end-point retorna um dicionário com as informações e preços das
    criptomoedas solicitadas.

    Retorna:
        (Tuple[Response, int])
    """

    try:
        # Extrai os valores dos headers
        headers = headers_validator.HeadersValidator.from_headers(request.headers)

    except ValidationError as e:
        # Retorna 400 caso haja erros de validação nos headers
        abort(400, description=f"Malformed headers: {str(e)}")

    # Converte os valores de price_change_percentage de string para lista
    price_change_percentage = convert_change_percentage.execute(
        price_change_percentage_1h=headers.price_change_percentage_1h,
        price_change_percentage_24h=headers.price_change_percentage_24h,
        price_change_percentage_7d=headers.price_change_percentage_7d,
        price_change_percentage_14d=headers.price_change_percentage_14d,
        price_change_percentage_30d=headers.price_change_percentage_30d,
        price_change_percentage_200d=headers.price_change_percentage_200d,
        price_change_percentage_1y=headers.price_change_percentage_1y
    )

    # Chama a função para obter as informações das criptomoedas
    infos, status = get_infos.execute(
        order=headers.order,
        per_page=headers.per_page,
        price_change_percentage=price_change_percentage
    )

    if status != 200:
        # Retorna o status e a descrição de erro caso haja erros na API de criptomoedas
        abort(
            status,
            description=infos.get(
                'error', 
                infos.get('status', {}).get('error_message', 'Unknown error')
            )
        )

    # Chama a função para obter os preços das criptomoedas
    prices, status = get_prices.execute(
        ids=[coin["id"] for coin in infos],
        include_market_cap=headers.include_market_cap,
        include_24hr_vol=headers.include_24hr_vol,
        include_24hr_change=headers.include_24hr_change,
        include_last_updated_at=headers.include_last_updated_at
    )

    if status != 200:
        # Retorna o status e a descrição de erro caso haja erros na API de preços
        abort(
            status,
            description=prices.get(
                'error', 
                prices.get('status', {}).get('error_message', 'Unknown error')
            )
        )

    # Chama a função para mesclar as informações com os preços
    response = join_data_info_price.execute(
        infos=infos,
        prices=prices
    )

    # Retorna o dicionário com as informações e preços das criptomoedas
    return jsonify(response), 200
