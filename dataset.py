import requests
import json

api_key = '79fWD7OC8t6l1usTOZcvX3mD1H94jNAs8AUnhTjs'

url='https://api.chart-img.com/v2/tradingview/advanced-chart'


headers = {
    'x-api-key': api_key,
    'content-type': 'application/json'
   }

payload = {
    "symbol": "OANDA:EURUSD",
    "interval": "1h",
}

response = requests.post(url, headers=headers, data=json.dumps(payload))

if response.status_code == 200:
    with open('chart-img-advanced.png', 'wb') as file:
        file.write(response.content)
    
    print('Chart image saved as chart-img.png')
    
else:
    print('Failed to get the chart image:', response.text)
