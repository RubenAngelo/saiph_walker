# 🚀 Saiph Walker API

**API RESTful** construída com **Flask** que fornece informações e preços atualizados de criptomoedas,
permitindo o controle detalhado de resposta através de headers HTTP.
A API também conta com limitação de requisições, tratamento robusto de erros, e estrutura modular para escalabilidade e manutenção.

## ✨ Funcionalidades

- 📈 Obtenção de dados de preços e variação de criptomoedas da API da CoinGecko via **Requests**.
- 🧩 Customização das informações via headers HTTP.
- 🛡️ Validação de headers com **Pydantic**.
- ⚙️ Modularidade com **Blueprints**.
- 📉 Rate limiting com **Flask-Limiter** (3 requisições por minuto por IP).
- 📋 Logs detalhados de requisições e respostas com o **logging**.
- ⚠️ Tratamento completo de erros HTTP com respostas padronizadas com o **errorhandler** do **Flask**.

## 🗂️ Estrutura do Projeto

``` python
/SAIPH_WALKER
├── app
│   ├── routes
│   │   └── v1
│   │       └── cripto
│   │           └── info_price.py   # Rota principal da API
│   ├── functions                   # Funções auxiliares da API
│   ├── handler                     # Tratadores de erro
│   ├── util                        # Utilitários (e.g., logs, tempo)
│   ├── logs/                       # Logs da API
│   └── __init__.py                 # Factory da aplicação Flask
├── run.py                          # Arquivo de execução da aplicação
├── requirements.txt
└── README.md
```