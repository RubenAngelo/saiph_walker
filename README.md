# 🚀 Saiph Walker API

**API RESTful** construída com **Flask** que fornece informações e preços atualizados de criptomoedas\,
permitindo o controle detalhado de resposta através de headers HTTP.
A API também conta com limitação de requisições, tratamento robusto de erros, e estrutura modular para escalabilidade e manutenção\.

---

## ✨ Funcionalidades

- 📈 Obtenção de dados de preços e variação de criptomoedas da API da CoinGecko via **Requests**.
- 🧩 Customização das informações via headers HTTP.
- 🛡️ Validação de headers com **Pydantic**.
- ⚙️ Modularidade com **Blueprints**.
- 📉 Rate limiting com **Flask-Limiter** (3 requisições por minuto por IP).
- 📋 Logs detalhados de requisições e respostas com o **logging**.
- ⚠️ Tratamento completo de erros HTTP com respostas padronizadas com o **errorhandler** do **Flask**.

---

## 🗂️ Estrutura do Projeto

~~~~ python
/SAIPH_WALKER
├── app
│   ├── constant
│   │   └── constants.py
|   |
│   ├── functions
|   |   ├── convert_change_percentage.py
|   |   ├── get_infos.py
|   |   ├── get_prices.py
|   |   ├── headers_validator.py
|   |   └── logger_config.py
|   |
│   ├── handler
│   │   └── handlers.py
│   │
│   ├── routes
|   |   └── v1
|   |       ├── cripto
|   |       |   └── info_price.py
|   |       |
|   |       ├── health
|   |       |   └── check.py
|   |       |
|   |       ├── __init__.py
|   |       └── blueprints.py
|   |
│   ├── util
|   |   └── utils.py
│   │
│   └── __init__.py
│
├── logs
│   └── app_yyyy-MM-dd_hh-mm.log
│
├── README.md                               
├── requirements.txt                        
└── run.py                                  
~~~~

---

## 📌 Rota Principal

`GET /api/saiphwalker/v1/cripto/info/price/execute`


**Descrição**:
Consulta informações de criptomoedas da API publica da CoinGecko com suporte a personalização da resposta via headers HTTP.

---

## Headers

|            Header            |  Tipo  |                                   Descrição                                    |  Valor padrão   |                           Valores aceitos                            |
|:----------------------------:|:------:|:------------------------------------------------------------------------------:|:---------------:|:--------------------------------------------------------------------:|
|            Order             | string |                 Ordem de exibição das criptomoedas no response                 | market_cap_desc | market_cap_desc,market_cap_asc,volume_asc,volume_desc,id_asc,id_desc |
|           Per-Page           | string |                      Número de criptomoedas por response                       |      top_5      |     top_1,top_2,top_3,top_4,top_5,top_6,top_7,top_8,top_9,top_10     |
|      Include-Market-Cap      | string |              Incluir capitalização de mercado de cada criptomoeda              |      true       |                              true,false                              |
|       Include-24Hr-Vol       | string |               Incluir volume das últimas 24h de cada criptomoeda               |      true       |                              true,false                              |
|     Include-24Hr-Change      | string |                  Incluir variação das 24h de cada criptomoeda                  |      true       |                              true,false                              |
|   Include-Last-Updated-At    | string |                  incluir a data da última atualização em UNIX                  |      true       |                              true,false                              |
|  Price-Change-Percentage-1H  | string |    incluir variação percentual de preço da última hora de cada criptomoeda     |      false      |                              true,false                              |
| Price-Change-Percentage-24H  | string |     incluir variação percentual de preço do último dia de cada criptomoeda     |      true       |                              true,false                              |
|  Price-Change-Percentage-7D  | string |   incluir variação percentual de preço da última semana de cada criptomoeda    |      true       |                              true,false                              |
| Price-Change-Percentage-14D  | string | incluir variação percentual de preço das últimas 2 semanas de cada criptomoeda |      false      |                              true,false                              |
| Price-Change-Percentage-30D  | string |     incluir variação percentual de preço do último mês de cada criptomoeda     |      true       |                              true,false                              |
| Price-Change-Percentage-200D | string | incluir variação percentual de preço dos últimos 200 dias de cada criptomoeda  |      false      |                              true,false                              |
|  Price-Change-Percentage-1Y  | string |     incluir variação percentual de preço do último ano de cada criptomoeda     |      false      |                              true,false                              |

---

## Exemplo de Requisição

~~~~ bash
curl -X GET 'http://localhost:5000/api/saiphwalker/v1/cripto/info/price/execute' \
--header 'Order: market_cap_desc' \
--header 'Per-Page: top_1' \
--header 'Include-Market-Cap: true' \
--header 'Include-24Hr-Vol: true' \
--header 'Include-24Hr-Change: true' \
--header 'Include-Last-Updated-At: true' \
--header 'Price-Change-Percentage-1H: false' \
--header 'Price-Change-Percentage-24H: true' \
--header 'Price-Change-Percentage-7D: true' \
--header 'Price-Change-Percentage-14D: false' \
--header 'Price-Change-Percentage-30D: true' \
--header 'Price-Change-Percentage-200D: false' \
--header 'Price-Change-Percentage-1Y: false'
~~~~

---

## Exemplo de Resposta (200 OK)

~~~~ json
[
    {
        "ath": 108786,
        "ath_change_percentage": -22.75336,
        "ath_date": "2025-01-20T09:11:54.494Z",
        "atl": 67.81,
        "atl_change_percentage": 123826.26824,
        "atl_date": "2013-07-06T00:00:00.000Z",
        "circulating_supply": 19840603.0,
        "current_price": 84098,
        "fully_diluted_valuation": 1668499390896,
        "high_24h": 84492,
        "id": "bitcoin",
        "image": "https://coin-images.coingecko.com/coins/images/1/large/bitcoin.png?1696501400",
        "last_updated": "2025-03-23T02:29:06.423Z",
        "last_updated_at": 1742696940,
        "low_24h": 83709,
        "market_cap": 1668499390896,
        "market_cap_change_24h": -1341764236.9660645,
        "market_cap_change_percentage_24h": -0.08035,
        "market_cap_rank": 1,
        "max_supply": 21000000.0,
        "name": "Bitcoin",
        "price_change_24h": -67.03527112344455,
        "price_change_percentage_24h": -0.07965,
        "price_change_percentage_24h_in_currency": -0.07964753311720274,
        "price_change_percentage_30d_in_currency": -14.507040396189216,
        "price_change_percentage_7d_in_currency": 0.23645445093731804,
        "roi": null,
        "symbol": "btc",
        "total_supply": 19840603.0,
        "total_volume": 8255654276,
        "usd": 84095,
        "usd_24h_change": -0.08277171377021249,
        "usd_24h_vol": 8254290175.502451,
        "usd_market_cap": 1668499390896.371
    },
]
~~~~

---

## 📌 Rota de Checagem da API

`GET /api/saiphwalker/v1/health/check`

**Descrição**:
Consulta o status da versão da API.

---

## Exemplo de Requisição

~~~~ bash
curl -X GET http://localhost:5000/api/saiphwalker/v1/health/check/'
~~~~

---

## Exemplo de Resposta (200 OK)

~~~~ json
{
    "status": "(V1) To the Orion, my friend!",
    "status_code": 200,
    "timestamp": 1742707788.380798
}
~~~~

---

## 🧪 Como Rodar Localmente

1. Clone o repositório

    ~~~~ bash
    git clone https://github.com/RubenAngelo/saiph_walker.git
    cd saiph_walker
    ~~~~

2. Instale as dependências

    ~~~~ bash
    pip install -r requirements.txt
    ~~~~

3. Execute a aplicação

    ~~~~ bash
    python run.py
    ~~~~

    >[!NOTE]
    >
    >Crie um .env ou insira as variáveis `BASE_URL = https://api.coingecko.com/api/v3` e `KEY = Sua chave de API da CoinGecko` no seu ambiente.
    ><https://docs.coingecko.com/v3.0.1/reference/setting-up-your-api-key>

---

## 📝 Logs

- Os logs são gerados automaticamente em /root/logs/ com data e hora no nome do arquivo.
- Cada requisição e resposta é registrada com detalhes:
  - Método, rota, headers, corpo.
  - Status e corpo da resposta.
  - Erros são também logados com tracebacks (se houver).

---

## ⚠️ Limitação de Requisições

- Cada IP pode fazer até 3 requisições por minuto para as rotas `/api/saiphwalker/v1/cripto/info/price/execute` e `/api/saiphwalker/v1/health/check`.

---

## 🛠️ Tecnologias Utilizadas

- Python
- Flask
- Pydantic
- Flask-Limiter
- Logging

---

## 💡 Contribuindo

Sinta-se à vontade para abrir issues ou pull requests. Feedbacks e melhorias são sempre bem-vindos!

---

## 🤝 Contato

Desenvolvido por [Ruben Adriel Angelo Gomes](https://www.linkedin.com/in/ruben-adriel-angelo-gomes/)  
📧 Email: <ruben.a.angelo@gmail.com>