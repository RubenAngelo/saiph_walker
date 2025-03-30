# 🚀 Saiph Walker API V2

**API RESTful** construída com **Flask** que fornece informações e preços atualizados de criptomoedas,
permitindo o controle detalhado de resposta através de headers HTTP.
A API também conta com limitação de requisições, tratamento robusto de erros, conexão com banco de dados postgreSQL, e estrutura modular para escalabilidade e manutenção.

---

## ✨ Funcionalidades

- 📈 Obtenção de dados de preços e variação de criptomoedas da API da CoinGecko via **Requests**.
- 🧩 Customização das informações via headers HTTP.
- 🛡️ Validação de headers com **Pydantic**.
- ⚙️ Modularidade com **Blueprints**.
- 📉 Rate limiting com **Flask-Limiter** (3 requisições por minuto por IP).
- 📋 Logs detalhados de requisições e respostas com o **logging**.
- ⚠️ Tratamento completo de erros HTTP com respostas padronizadas com o **errorhandler** do **Flask**.
- 📅 Rotina criada para chamar a API à cada 5 minutos com o **apscheduler**.
- 📊 Conexão com um banco de postgreSQL com o **psycopg2**

</br>

## 🗂️ Estrutura do Projeto

~~~~ python
/SAIPH_WALKER
├── app
│   ├── config
│   │   ├── db_config.py
│   │   └── logger_config.py
│   │
│   ├── constant
│   │   └── constants.py
│   │
│   ├── functions
│   │   ├── convert_change_percentage.py
│   │   ├── get_infos.py
│   │   ├── get_prices.py
│   │   ├── headers_validator.py
│   │   ├── join_data_info_price.py
│   │   └── saiphwalker_caller.py
│   │
│   ├── handler
│   │   └── error_handlers.py
│   │
│   ├── routes
│   │   └── v2
│   │       ├── cripto
│   │       │   └── info_price.py
│   │       │
│   │       ├── health
│   │       │   └── check.py
│   │       │
│   │       ├── __init__.py
│   │       └── blueprints.py
│   │
│   ├── sql
│   │    ├── insert_into_mintaka.sql
│   │    └── create_table_mintaka.sql
│   │
│   ├── util
│   │   └── utils.py
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

</br>

## 📌 Endpoint de informação e preço das criptomoedas

### GET `/api/saiphwalker/v2/cripto/info/price/execute`

</br>

> [!NOTE]
> **Descrição**: Consulta informações de criptomoedas da API publica da CoinGecko com suporte a personalização da resposta via headers HTTP.
>
> A chamada da API ocorre automaticamente a cada 5 minutos ao iniciar a aplicação.
>
> A API V2 não tem output, ela insere os dados da CoinGecko no banco de dados.
>

> [!TIP]
> Para saber a estrutura dos dados acesse a [documentação da API V1.](https://github.com/RubenAngelo/saiph-walker/blob/main/app/routes/v1/README.md#-exemplo-de-resposta-200-ok)

- ## 🧾 Headers

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

- ## 📤 Exemplo de Requisição

    ~~~~ bash
    curl -X GET 'http://localhost:5000/api/saiphwalker/v2/cripto/info/price/execute' \
    --header 'Order: market_cap_desc' \
    --header 'Per-Page: top_5' \
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

- ## ✅ Exemplo de Resposta (204 No Content)

    ~~~~ json
    {}
    ~~~~

</br>

## 🔍 Endpoint de Status

### GET `/api/saiphwalker/v2/health/check`

</br>

> [!NOTE]
> **Descrição**: Consulta o status da API V2

- ## 📤 Exemplo de Requisição **Endpoint de Status**

    ~~~~ bash
    curl -X GET http://localhost:5000/api/saiphwalker/v2/health/check/'
    ~~~~

- ## ✅ Exemplo de Resposta (200 OK) **Endpoint de Status**

    ~~~~ json
    {
        "status": "(V2) To the Orion, my friend!",
        "status_code": 200,
        "timestamp": 1742707788.380798
    }
    ~~~~

</br>

## 🧪 Como Rodar Localmente

</br>

> [!IMPORTANT]
>
> Crie um .env ou insira as variáveis `BASE_URL = https://api.coingecko.com/api/v3` e `KEY = Sua chave de API da CoinGecko` no seu ambiente.
>
> [Documentação da CoinGecko para obter a chave de API.](https://docs.coingecko.com/v3.0.1/reference/setting-up-your-api-key)
> 
> No .env crie as seguintes variáveis ou insira as variáveis para conectar ao banco de dados
> - NAME_DB <sup> Nome do banco de dados. </sup>
> - USER_DB <sup> User do banco de dados. </sup>
> - PASSWORD_DB <sup> Senha do banco de dados. </sup>
> - HOST_DB <sup> Host do banco de dados. </sup>
> - PORT_DB <sup> Porta do banco de dados. </sup>
>

</br>

1. Clone o repositório

    ~~~~ bash
    git clone https://github.com/RubenAngelo/saiph_walker.git
    cd saiph_walker
    ~~~~

2. Instale as dependências

    ~~~~ bash
    pip install -r requirements.txt
    ~~~~

3. Crie a tabela no banco de dados
    - Use o [CREATE TABLE da tabela mintaka](https://github.com/RubenAngelo/saiph-walker/blob/main/app/sql/create_table_mintaka.sql)

4. Execute a aplicação

    ~~~~ bash
    python run.py
    ~~~~

</br>

## 📝 Logs

- Os logs são gerados automaticamente em /root/logs/ com data e hora no nome do arquivo.
- Cada requisição e resposta é registrada com detalhes:

  - Método, rota, headers, corpo.
  - Status e corpo da resposta.
  - Erros são também logados com tracebacks (se houver).

## ⚠️ Limitação de Requisições

- Cada IP pode fazer até 3 requisições por minuto para as rotas `/api/saiphwalker/v2/cripto/info/price/execute` e `/api/saiphwalker/v2/health/check`.

## 🛠️ Tecnologias Utilizadas

- Python
- Flask
- Pydantic
- Flask-Limiter
- Logging
- psycopg2

## 💡 Contribuindo

Sinta-se à vontade para abrir issues ou pull requests. Feedbacks e melhorias são sempre bem-vindos!  

## 🤝 Contato

Desenvolvido por [Ruben Adriel Angelo Gomes](https://www.linkedin.com/in/ruben-adriel-angelo-gomes/)  
📧 Email: <ruben.a.angelo@gmail.com>

---
