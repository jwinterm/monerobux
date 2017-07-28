import requests


url = 'https://api.coinmarketcap.com/v1/ticker/?bcc'

r = requests.get(url)
j = r.json()
for i in j:
    if i['id'] == 'bitcoin-cash':
        coin = i
symbol = coin['symbol']
name = coin['name']
rank = coin['rank']
price_usd = float(coin['price_usd'])
price_btc = float(coin['price_btc'])
volume_usd = float(coin['24h_volume_usd'])
percent_change_24h = float(coin['percent_change_24h'])
print("{0} ({1}) is #{2}. Last price ${3:.2f} / {4:.8f}. 24h volume ${5:,.0f} changed {6}%.}.".format(name, symbol, rank, price_usd, price_btc, volume_usd, percent_change_24h))

