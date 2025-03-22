import requests

headers = {
  'Vs-Currency': 'usd',
  'Order': 'market_cap_desc',
  'Per-Page': '5',
  'Price-Change-Percentage': '24h,7d,30d',
  'Include-Market-Cap': 'true',
  'Include-24Hr-Vol': 'true',
  'Include-24Hr-Change': 'true',
  'Include-Last-Updated-At': 'true'
}

# Fazendo uma requisição GET
response = requests.get('http://127.0.0.1:5000/saiphwalker', headers=headers, timeout=10)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    print(response.json())  # Exibe o conteúdo da resposta em formato JSON
else:
    print(f"Falha na requisição: {response.status_code}")

