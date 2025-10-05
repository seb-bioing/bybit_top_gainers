import requests
import time

def get_top_gainers():
    url = 'https://api.bybit.com/v5/market/tickers?category=linear'
    response = requests.get(url)
    data = response.json()

    if data['retCode'] == 0:
        tickers = data['result']['list']
        top_gainers = sorted(tickers, key=lambda x: float(x['price24hPcnt']), reverse=True)
        print("📈 Top 10 Gainers de Futuros en Bybit (24h):\n")
        for t in top_gainers[:10]:
            symbol = t['symbol']
            price = t['lastPrice']
            change_pct = float(t['price24hPcnt']) * 100
            volume = t['turnover24h']
            print(f"{symbol}: {change_pct:.2f}% | Precio: ${price} | Volumen 24h: {volume}")
    else:
        print("Error:", data['retMsg'])

while True:
    get_top_gainers()
    time.sleep(300)  # cada 5 minutos
