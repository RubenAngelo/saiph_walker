"""
Módulo para validar headers HTTP.

Este módulo fornece uma classe para validar headers HTTP,
garantindo que eles atendam às restrições definidas.

A classe HeadersValidator define a estrutura e as restrições para os headers,
permitindo a validação de headers de entrada.

Classes:
    HeadersValidator: Uma classe usada para validar headers HTTP.

Notas:
    A classe HeadersValidator utiliza a biblioteca Pydantic
    para definir as restrições e validar os headers.
"""
from typing import Dict

from pydantic import BaseModel, constr

class HeadersValidator(BaseModel):
    """
    Uma classe usada para validar headers HTTP.

    Ela define a estrutura e as restrições para os headers.
    """

    # Defina as restrições para os headers
    order: constr(
        pattern='^(market_cap_desc|market_cap_asc|volume_asc|volume_desc|id_asc|id_desc)$'
    ) = 'market_cap_desc' # type: ignore

    per_page: constr(
        pattern='^(top_1|top_2|top_3|top_4|top_5|top_6|top_7|top_8|top_9|top_10)$'
    ) = 'top_5' # type: ignore

    include_market_cap: constr(
        pattern='^(true|false)$'
    ) = 'true' # type: ignore

    include_24hr_vol: constr(
        pattern='^(true|false)$'
    ) = 'true' # type: ignore

    include_24hr_change: constr(
        pattern='^(true|false)$'
    ) = 'true' # type: ignore

    include_last_updated_at: constr(
        pattern='^(true|false)$'
    ) = 'true' # type: ignore

    price_change_percentage_1h: constr(
        pattern='^(true|false)$'
    ) = 'false' # type: ignore

    price_change_percentage_24h: constr(
        pattern='^(true|false)$'
    ) = 'true' # type: ignore

    price_change_percentage_7d: constr(
        pattern='^(true|false)$'
    ) = 'true' # type: ignore

    price_change_percentage_14d: constr(
        pattern='^(true|false)$'
    ) = 'false' # type: ignore

    price_change_percentage_30d: constr(
        pattern='^(true|false)$'
    ) = 'true' # type: ignore

    price_change_percentage_200d: constr(
        pattern='^(true|false)$'
    ) = 'false' # type: ignore

    price_change_percentage_1y: constr(
        pattern='^(true|false)$'
    ) = 'false' # type: ignore

    @classmethod
    def from_headers(cls: "HeadersValidator", headers: Dict[str, str]) -> "HeadersValidator":
        """
        Cria uma instância de HeadersValidator a partir dos headers HTTP.

        Este método extrai informações relevantes do dicionário de headers fornecido
        e inicializa um objeto HeadersValidator com os dados extraídos. Valores padrão
        são fornecidos caso certos headers não estejam presentes.

        Parâmetros:
            headers (Dict[str, str])

        Retorna:
            Tuple[dict, int]
        """

        # Extrai os valores dos headers com valores padrão e os converte para minúsculas
        data = {
            "order": headers.get(
                "Order", "market_cap_desc"
            ).lower(),

            "per_page": headers.get(
                "Per-Page", "top_5"
            ).lower(),

            "include_market_cap": headers.get(
                "Include-Market-Cap", "true"
            ).lower(),

            "include_24hr_vol": headers.get(
                "Include-24Hr-Vol", "true"
            ).lower(),

            "include_24hr_change": headers.get(
                "Include-24Hr-Change", "true"
            ).lower(),

            "include_last_updated_at": headers.get(
                "Include-Last-Updated-At", "true"
            ).lower(),

            "price_change_percentage_1h": headers.get(
                "Price-Change-Percentage-1H", "false"
            ).lower(),

            "price_change_percentage_24h": headers.get(
                "Price-Change-Percentage-24H", "true"
            ).lower(),

            "price_change_percentage_7d": headers.get(
                "Price-Change-Percentage-7D", "true"
            ).lower(),

            "price_change_percentage_14d": headers.get(
                "Price-Change-Percentage-14D", "false"
            ).lower(),

            "price_change_percentage_30d": headers.get(
                "Price-Change-Percentage-30D", "true"
            ).lower(),

            "price_change_percentage_200d": headers.get(
                "Price-Change-Percentage-200D", "false"
            ).lower(),

            "price_change_percentage_1y": headers.get(
                "Price-Change-Percentage-1Y", "false"
            ).lower(),
        }

        # Retorna uma instância de HeadersValidator inicializada com os dados extraídos
        return cls(**data)
