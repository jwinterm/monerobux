#romerito -*- coding: UTF-8 -*-
import sopel.module
import requests
import time
import random
import datetime
import re
import client
import csv

polourl = "https://poloniex.com/public?command=returnTicker"
poloxmrlendurl = "https://poloniex.com/public?command=returnLoanOrders&currency=XMR&limit=999999"
polobtclendurl = "https://poloniex.com/public?command=returnLoanOrders&currency=BTC&limit=999999"
prevamnt, prevtime = 0, 0
trexurl = "https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-"
finexbtc = 'https://api.bitfinex.com/v1/pubticker/XMRBTC'
finexusd = 'https://api.bitfinex.com/v1/pubticker/XMRUSD'
krakbtc = 'https://api.kraken.com/0/public/Ticker?pair=XMRXBT'
krakbtceur = 'https://api.kraken.com/0/public/Ticker?pair=XBTEUR'
krakusd = 'https://api.kraken.com/0/public/Ticker?pair=XMRUSD'
krakeur = 'https://api.kraken.com/0/public/Ticker?pair=XMREUR'
kraktrig = 'https://api.kraken.com/0/public/Ticker?pair='  #append coin/trigger in function below
krakusdt = 'http://api.kraken.com/0/public/Ticker?pair=USDTUSD'
bitflyerurl = 'https://api.bitflyer.jp/v1/ticker'
thumbxmrurl = 'https://api.bithumb.com/public/ticker/xmr'	# measured natively in KRW
thumbbtcurl = 'https://api.bithumb.com/public/ticker/btc'	# measured natively in KRW
binanceurl = 'https://api.binance.com/api/v1/ticker/24hr'
ogreurl = 'https://tradeogre.com/api/v1/markets'


@sopel.module.commands('ath')
def ath(bot, trigger):
    r = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=monero&order=market_cap_desc&per_page=100&page=1&sparkline=false')
    j= r.json()
    usdath = j[0]['ath']
    usdathdate = j[0]['ath_date']
    r = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=btc&ids=monero&order=market_cap_desc&per_page=100&page=1&sparkline=false')
    j= r.json()
    btcath = j[0]['ath']
    btcathdate = j[0]['ath_date']
    bot.say("BTC ath = {} on {}. USD ath = ${} on {}".format(btcath, btcathdate, usdath, usdathdate))


@sopel.module.commands('bfx', 'bitfinex')
def bfx(bot, trigger):
    stringtosay = ''
    try:
        r = requests.get(finexbtc)
        j = r.json()
        stringtosay += "Last XMR/BTC trade at {0:.6f} on {1:.2f} 24 h XMR volume. ".format(float(j['last_price']), float(j['volume']))
    except:
        bot.say("Error getting XMR/BTC data")
    try:
        r = requests.get(finexusd)
        j = r.json()
        stringtosay += "Last XMR/USD trade at {0:.2f} on {1:.2f} 24 h XMR volume.".format(float(j['last_price']), float(j['volume']))
    except:
        bot.say("Error getting XMR/USD data")
    try:
        bot.say(stringtosay)
    except:
        bot.say("Error getting data")


@sopel.module.commands('binance', 'cz')
def binance(bot, trigger):
    try:
        if not trigger.group(2):
             coin = 'XMR'
             pair = 'BTC'
        else:
            coin = trigger.group(2).split(' ')[0].upper()
            try:
                if len(trigger.group(2).split(' ')[1]) > 1:
                    pair = trigger.group(2).split(' ')[1].upper()
                else:
                    pair = "BTC"
            except:
                pair = "BTC"
        r = requests.get(binanceurl)
        j = r.json()
        found = False
        for i in j:
            if i["symbol"] == coin+pair:
                last=float(i['lastPrice'])
                change=float(i['priceChangePercent'])
                vol=float(i['volume'])
                bot.say("{0} on Binance at {1:.8f} {2}; {3:.2f}% over 24 hours on {4:.3f} {2} volume".format(coin, last, pair, change, vol*last))
                found = True
        if found == False:
            bot.say("Too scammy even for Binance")
    except:
        bot.say("Error retrieving data from Binance")


@sopel.module.commands('btckrak', 'btckraken', 'btceur')
def krakeur(bot, trigger):
    stringtosay = ''
    try:
        r = requests.get(krakbtceur)
        j = r.json()
        stringtosay += "Last BTC/EUR trade at €{0:.2f} on {1:.2f} BTC 24 h volume. ".format(float(j['result']['XXBTZEUR']['c'][0]), float(j['result']['XXBTZEUR']['v'][0]))
    except:
        bot.say("Error getting BTC/EUR data")
    try:
        bot.say(stringtosay)
    except:
        bot.say("Error getting data")


@sopel.module.commands('btclending')
def btclending(bot, trigger):
    try:
        r=requests.get(polobtclendurl)
        j=r.json()
        amnt=0
        amnt10=0
        rate10=0
        amnt100=0
        rate100=0
        for i in j['offers']:
            if amnt < 10:
                amnt10=amnt
                rate10=float(i['rate'])
            if amnt < 100:
                amnt100=amnt
                rate100=float(i['rate'])
            amnt+=float(i['amount'])
        bot.say("Minimum rate is {0:.3f}%. To borrow {1:,.2f} BTC need up to rate {2:.3f}%. To borrow {3:,.2f} BTC need up to rate {4:.3f}%. Total amount is {5:,.2f} BTC at max rate {6:.3f}%".format(float(j['offers'][0]['rate'])*100, amnt10, rate10*100, amnt100, rate100*100, amnt, float(j['offers'][-1]['rate'])*100))
    except:
        bot.say("Something bad happened :o")


@sopel.module.commands('cmc', 'coinmarketcap')
def cmc(bot, trigger):
    bot.say("fuck cmc and their scam promoting website")


@sopel.module.commands('gecko', 'cg', 'gec')
def gecko(bot, trigger):
    if not trigger.group(2):
        coin = "monero"
    else:
        coin = trigger.group(2).lower()
    try:
        r = requests.get('https://api.coingecko.com/api/v3/coins/list')
        j = r.json()
        for i in j:
            if coin == i['symbol'] or coin == i['name'].lower():
                id = i['id']
    except:
        bot.say("Failed to find {}".format(coin))
    try:
        if coin == 'wow' or coin == 'wownero': id = 'wownero'
        r = requests.get('https://api.coingecko.com/api/v3/coins/'+id)
        j = r.json()
        name = j['name']
        ticker = j['symbol'].upper()
        mcaprank = j['market_cap_rank']
        mcap = j['market_data']['market_cap']['usd']
        geckorank = j['coingecko_rank']
        btcprice = j['market_data']['current_price']['btc']
        usdprice = j['market_data']['current_price']['usd']
        athbtc = j['market_data']['ath']['btc']
        athusd = j['market_data']['ath']['usd']
        change_1d = j['market_data']['price_change_percentage_24h_in_currency']['usd']
        change_1w = j['market_data']['price_change_percentage_7d_in_currency']['usd']
        try:
            change_1m = j['market_data']['price_change_percentage_30d_in_currency']['usd']
        except: change_1m = 0
        try:
            change_1y = j['market_data']['price_change_percentage_1y_in_currency']['usd']
        except: change_1y = 0
        bot.say("{} ({}) is #{:.0f} by mcap (${:.2e}) and #{:.0f} by coingecko rank. Current price is {:.8f} BTC / ${:.3f}. ATH price is {:.8f} BTC / ${:.3f}. USD change: 1d {:.1f}%, 1w {:.1f}%, 1m {:.1f}%, 1y {:.1f}%.".format(name, ticker, mcaprank, mcap, geckorank, btcprice, usdprice, athbtc, athusd, change_1d, change_1w, change_1m, change_1y))
    except:
        bot.say("Failed to retrieve or parse data for {}".format(coin))

@sopel.module.commands('coin', 'coinex')
def coinex(bot, trigger):
    if not trigger.group(2):
        bot.say(".coin <coin-name> <currency-code>")
    else:
        try:
            coinname = trigger.group(2).split(" ")[0]
            currencyname = trigger.group(2).split(" ")[1]
            r = requests.get(
                'https://api.coingecko.com/api/v3/coins/markets?vs_currency={0}&ids={1}&sparkline=false'.
                format(currencyname, coinname))
            j = r.json()
            bot.say("{0} price {1:,.2f} {2}".format(j[0]['name'],
                                                    float(
                                                        j[0]['current_price']),
                                                    currencyname.upper()))
        except:
            bot.say("Failed to retrieve price.")

@sopel.module.commands('krak', 'kraken')
def krak(bot, trigger):
    stringtosay = ''
    if not trigger.group(2):
        try:
            r = requests.get(krakbtc)
            j = r.json()
            stringtosay += "Last XMR/BTC trade at {0:.6f} on {1:.2f} 24 h XMR volume. ".format(float(j['result']['XXMRXXBT']['c'][0]), float(j['result']['XXMRXXBT']['v'][1]))
        except:
            bot.say("Error getting XMR/BTC data")
        try:
            r = requests.get(krakusd)
            j = r.json()
            stringtosay += "Last XMR/USD trade at {0:.2f} on {1:.2f} 24 h XMR volume. ".format(float(j['result']['XXMRZUSD']['c'][0]), float(j['result']['XXMRZUSD']['v'][1]))
        except:
            bot.say("Error getting XMR/USD data")
        try:
            r = requests.get('https://api.kraken.com/0/public/Ticker?pair=XMREUR')  #shouldn't this be krakeur?
            j = r.json()
            stringtosay += "Last XMR/EUR trade at {0:.2f} on {1:.2f} 24 h XMR volume. ".format(float(j['result']['XXMRZEUR']['c'][0]), float(j['result']['XXMRZEUR']['v'][1]))
        except:
            bot.say("Error getting XMR/EUR data")
        try:
            bot.say(stringtosay)
        except:
            bot.say("Error getting data")
    else:
        coin = trigger.group(2).upper()
        try:
            r=requests.get(kraktrig+coin+'XBT')
            j=r.json()
            stringtosay += "{0} at {1:.8f} on {2:.2f} 24 h {0} volume. ".format(coin, float(j['result']['X'+str(coin)+'XXBT']['c'][0]), float(j['result']['X'+str(coin)+'XXBT']['v'][1]))
        except:
            bot.say("Error connecting to Kraken")
        try:
            bot.say(stringtosay)
        except:
            bot.say("Error getting data")


@sopel.module.commands('lending')
def lending(bot, trigger):
    try:
        r=requests.get(poloxmrlendurl)
        j=r.json()
        amnt=0
        currenttime=time.time()
        for i in j['offers']:
            amnt+=float(i['amount'])
        global prevamnt
        prevamnt=amnt
        global prevtime
        prevtime=currenttime
        bot.say("Total amount of XMR available {0:,.2f}. Changed by {1:.2f} in the last {2:.2f} hours".format(amnt, amnt-prevamnt, (currenttime-prevtime)/3600))
    except:
        bot.say("Something bad happened :o")

@sopel.module.commands('chart')
def chart(bot, trigger):
    bot.say('https://cryptowat.ch/poloniex/xmrbtc')


@sopel.module.commands('metal')
def metal(bot, trigger):
    try:
        if not trigger.group(2):
            target = "Gold"
        elif trigger.group(2).lower() in {'xau', 'gold'}: target = "Gold"
        elif trigger.group(2).lower() in {'xag', 'silver'}: target = "Silver"
        elif trigger.group(2).lower() in {'xpd', 'palladium'}: target = "Palladium"
        elif trigger.group(2).lower() in {'xpt', 'platinum'}: target = "Platinum"
        pattern = re.compile('<div class=\"metal\">{}</div>\\r\\n\s*<div class=\"price\"><span class=\"current\">(\$[\d,.]*)</span><span class=\"([\w\s]*)\">\(?(\$[\d,.]*)'.format(target))
        r = requests.get('https://www.apmex.com/')
        result = re.findall(pattern, r.text)
        if 'green' in result[0][1]: sign = '+'
        else: sign = '-'
        bot.say("Last price for {} is {} with {}{} change".format(target, result[0][0], sign, result[0][2]))
    except:
        bot.say("Regex parsing of apmex failed")


@sopel.module.commands('polo', 'poloniex', 'marco', 'plol')
def polo(bot, trigger):
    if not trigger.group(2):
        try:
            r=requests.get(polourl)
            j=r.json()
            xmr=j["BTC_XMR"]
            last=float(xmr['last'])
            change=float(xmr['percentChange'])
            vol=float(xmr['baseVolume'])
            if change >= 0:
                sign = '+'
            else:
                sign = ''
            face = u'\u0000'
            if change > 0.10:
                face = u'\u263d'
            if 0.10 >= change > 0.05:
                face = u'\u2661'
            if 0.05 >= change > 0.02:
                face = u'\u263a'
            if 0.02 >= change > -0.02:
                face = u'\u2694'
            if -0.02 >= change > -0.05:
                face = u'\u2639'
            if -0.05 >= change > -0.1:
                face = u'\u2620'
            if change < -0.1:
                face = u'\u262d'
            bot.say("Poloniex at {0:.8f} BTC; {1}{2:.2f}% over 24 hours on {3:.3f} BTC volume {4}".format(last, sign, change*100, vol, face))
        except:
            bot.say("Error retrieving data from Poloniex")
    else:
        coin = trigger.group(2).upper()
        try:
            r=requests.get(polourl)
            j=r.json()
        except:
            bot.say("Error connecting to Poloniex")
        if len(coin) > 5 or len(coin) < 2:
            bot.say("Coin ticker is too long or short")
        # elif coin == "PASC":
        #     bot.say("COBOL only in #monero-markets")
        # elif coin == "NAUT":
        #     bot.say("That ship has sailed...")
        elif coin == "PIVX":
            bot.say("Masternodes + PoS...what could possibly go wrong?")
        else:
            label="BTC_" + coin
            try:
                ticker=j[label]
                last=float(ticker['last'])
                change=float(ticker['percentChange'])
                vol=float(ticker['baseVolume'])
                if change >= 0:
                    sign = '+'
                else:
                    sign = ''
                bot.say("{0} at {1:.8f} BTC; {2}{3:.2f}% over 24 hours on {4:.3f} BTC volume".format(coin, last, sign, change*100, vol))
            except:
                bot.say("ERROR!")


@sopel.module.commands('paprika', 'pap')
def paprika(bot, trigger):
    if not trigger.group(2):
        target = 'xmr'
    else: target = trigger.group(2).lower()
    try:
        r = requests.get('https://api.coinpaprika.com/v1/coins')
        j = r.json()
        if target.isdigit():
            for i in j:
                if int(target) == int(i['rank']):
                    id = i['id']
        else:
            for i in j:
                if target == i['name'].lower() or target == i['symbol'].lower():
                    id = i['id']
        r = requests.get('https://api.coinpaprika.com/v1/tickers/{}'.format(id))
        j = r.json()
        bot.say("{} ({}) is #{} by marketcap (${:.2e}), trading at ${:.4f} with a 24h vol of ${:.2e}. It's changed {}% over 24h, {}% over 7d, {}% over 30d, and {}% over 1y with an ath of ${} on {}.".format(j['name'], j['symbol'], j['rank'], float(j['quotes']['USD']['market_cap']), float(j['quotes']['USD']['price']), float(j['quotes']['USD']['volume_24h']), j['quotes']['USD']['percent_change_24h'], j['quotes']['USD']['percent_change_7d'], j['quotes']['USD']['percent_change_30d'], j['quotes']['USD']['percent_change_1y'], j['quotes']['USD']['ath_price'], j['quotes']['USD']['ath_date']))
    except:
        bot.say('No paprika only salt')

@sopel.module.commands('price')
def price(bot, trigger):
    if not trigger.group(2):
        bot.say("1 XMR = $12,345 USD (Offer valid in participating locations)")
    else:
        try:
            currency = trigger.group(2)
            r = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency={}&ids=monero&sparkline=false'.format(currency))
            j = r.json()
            bot.say("Monero price {0:,.2f} {1}".format(float(j[0]['current_price']), currency.upper()))
        except:
            bot.say("Failed to retrieve price.")


@sopel.module.commands('stock')
def stock(bot, trigger):
    ak = client.stocks_key
    if trigger.group(2):
        ticker = trigger.group(2).upper()
    else: ticker = 'WOW'
    try:
        r = requests.get('https://finnhub.io/api/v1/quote?symbol={}&token={}'.format(ticker, ak))
        j = r.json()
        date = j['t']
        high = j['h']
        low = j['l']
        last = j['c']
        pc = j['pc']
        bot.say("On {} {} had a high of {:.2f}, a low of {:.2f}, and last price of {:.2f} w/ {:.2f}% change".format(datetime.datetime.fromtimestamp(date), ticker, high, low, last, float(((last-pc)/pc))*100))
    except:
        bot.say("Can't find {}".format(ticker))


@sopel.module.commands('tradeogre', 'ogre')
def ogre(bot, trigger):
    if not trigger.group(2):
        pair = 'BTC-XMR'
    elif "hidden" in trigger.group(2) or "gem" in trigger.group(2):
        pair = 'BTC-WOW'
    else:
        pair = 'BTC-'+trigger.group(2).upper()
    try:
        r = requests.get(ogreurl)
        j = r.json()
        for i in j:
            if pair == i.keys()[0]:
                last=float(i[pair]['price'])
                vol=float(i[pair]['volume'])
        bot.say("{0} on Tradeogre at {1:.8f} BTC on {2:.3f} BTC volume".format(pair, last, vol))
    except:
        bot.say("Error retrieving data from Ogre")


@sopel.module.commands('trex', 'bittrex')
def trex(bot, trigger):
    geturl = ""
    if not trigger.group(2):
         bot.say("spineless...")
         return
    else:
        if trigger.group(2) == "xmr":
            bot.say("spineless")
            return
        else:
            geturl = trexurl + trigger.group(2)
    try:
        r = requests.get(geturl)
        j = r.json()
        xmr=j['result'][0]
        last=float(xmr['Last'])
        change=((last/float(xmr['PrevDay']))-1)
        vol=float(xmr['BaseVolume'])
        bot.say("Bittrex at {0:.8f} BTC; {1:.2f}% over 24 hours on {2:.3f} BTC volume".format(last, change*100, vol))
    except:
        bot.say("Error retrieving data from Bittrex")


@sopel.module.commands('top')
def top(bot, trigger):
    topXstring = ""
    try:
        try:
            r = requests.get('https://api.coingecko.com/api/v3/global')
            j = r.json()
            usd_total_mkt_cap = float(j['data']['total_market_cap']['usd'])
            rounded_total_mcap = trim_mcap(usd_total_mkt_cap)
            topXstring += "Total market cap $" + rounded_total_mcap + " | "
        except:
        	bot.say("Can't connect to coingecko API")
        if not trigger.group(2):
            try:
                r = requests.get('https://api.coingecko.com/api/v3/coins/'+'monero')
                j = r.json()
                mcaprank = j['market_cap_rank']
                if mcaprank > 20:
                    limit = mcaprank
                else:
                    limit = 20
            except:
                limit = 20
        else:
            limit = int(trigger.group(2))
            if limit > 30:
                bot.say("Too high!  Max is 30!")
                limit = 30
            elif limit < 1:
                bot.say("Dude...")
                return
        r = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page={}&page=1&sparkline=false'.format(limit))
        j = r.json()
        for i in j:
            symbol = i['symbol']
            name = i['name']
            rank = i['market_cap_rank']
            price_usd = float(i['current_price'])
            market_cap_usd = float(i['market_cap'])
            rounded_mcap = trim_mcap(market_cap_usd)
            topXstring += "{0}. {1} ${2} | ".format(rank, symbol, rounded_mcap) #TODO: add price_usd, rounded
        xmr_str = topXstring[-32:] # monero is at the end, and might get truncated
        final = (topXstring[:350] + " {...} " + xmr_str) if len(topXstring) > 350 else topXstring
        bot.say(final[:-2])
    except:
        bot.say("The use is 'top' and then a digit 1 - 20")

def trim_mcap(val):
    mcap = 0
    magnitude_sym = "M"
    if val >= 1e12: # >= 1T
        magnitude_sym = "T"
        if val >= 1e13:
          mcap = round(val/float(1e12),1) # >= 10T show one decimal
        else:
          mcap = round(val/float(1e12),2) # 1T <= x < 10T show two decimals
    elif val >= 1e9: # >= 1B
        magnitude_sym = "B"
        if val >= 1e11:
          mcap = int(round(val/float(1e9),0)) # >= 100B show no decimals
        else:
          mcap = round(val/float(1e9),1) # 1B <= x < 100B show one decimal
    else: # < 1B
      # mcap = "tiny"
      mcap = int(round(val/float(1e6),0)) # < 1B show no decimals
    rounded_mcap = str(mcap) + magnitude_sym
    return rounded_mcap

@sopel.module.commands('tall')
def tall(bot, trigger):
    stringtosend = ''
    stampurl = 'https://www.bitstamp.net/api/ticker/'
    finexurl = 'https://api.bitfinex.com/v1/pubticker/BTCUSD'
    btccurl  = 'https://data.btcchina.com/data/ticker?market=btccny'
    gemiurl  = 'https://api.gemini.com/v1/pubticker/btcusd'
    gdaxurl  = 'https://api.gdax.com/products/BTC-USD/ticker'
    # Bitstamp
    try:
        stampresult = requests.get(stampurl)
        stampjson = stampresult.json()
    except:
        stampjson = False
    if stampjson:
        stringtosend += "Bitstamp last: ${0:,.2f}, vol: {1:,.1f} | ".format(float(stampjson['last']), float(stampjson['volume']))
    # Gemini
    try:
        gemiresult = requests.get(gemiurl)
        gemijson = gemiresult.json()
    except:
        gemijson = False
    if gemijson:
        try:
            stringtosend += "Gemini last: ${0:,.2f}, vol: {1:,.1f} | ".format(float(gemijson['last']), float(gemijson['volume']['BTC']))
        except:
            pass
    # Gdax
    try:
        gdaxresult = requests.get(gdaxurl)
        gdaxjson = gdaxresult.json()
        gdaxprice = float(gdaxjson['price'])
        gdaxvolume = float(gdaxjson['volume'])
    except:
        gdaxjson = False
    if gdaxjson:
        stringtosend += "CBP last: ${0:,.2f}, vol: {1:,.1f} | ".format(gdaxprice, gdaxvolume)
    # Binance
    try:
        binanceresult = requests.get(binanceurl)
        binancejson = binanceresult.json()
        for i in binancejson:
            if i["symbol"] == "BTCUSDT":
                binanceprice = float(i['lastPrice'])
                binancevolume = float(i['volume'])
    except:
        binancejson = False
    if binancejson:
        stringtosend += "Binance last: ${0:,.2f}, vol: {1:,.1f} | ".format(binanceprice, binancevolume)
    # Bitfinex
    try:
        finexresult = requests.get(finexurl)
        finexjson = finexresult.json()
    except:
        finexjson = False
    try:
        if finexjson:
            stringtosend += "Bitfinex last: ${0:,.2f}, vol: {1:,.1f} | ".format(float(finexjson['last_price']), float(finexjson['volume']))
    except:
        stringtosend += "Finex sucks | "
    # Krak euro price
    try:
        r = requests.get(krakbtceur)
        j = r.json()
        stringtosend += "Kraken last: €{0:,.2f}, vol: {1:,.1f} | ".format(float(j['result']['XXBTZEUR']['c'][0]), float(j['result']['XXBTZEUR']['v'][0]))
    except:
        bot.say("Error getting BTC/EUR data")
    # Send the tickers to IRC
    bot.say(stringtosend[:-2])

addys = []
@sopel.module.commands('uni')
def uni(bot, trigger):
    addy = trigger.group(2)
    if len(addy) == 42 and addy[0:2] == "0x":
        try:
            r = requests.get("https://api.ethplorer.io/getTokenInfo/{}?apiKey=freekey".format(addy))
            j = r.json()
            name = j["name"]
            symbol = j["symbol"]
            holders = j["holdersCount"]
            price = j["price"]["rate"]
            mcap = j["price"]["marketCapUsd"]
            vol = j["price"]["volume24h"]
            bot.say("{} ({}) last price ${:.2f} on {:.2e} vol. Marketcap is ${:.2e} with {:.0f} addresses holding.".format(name, symbol, price, vol, mcap, holders))
            existflag = False
            for i in addys:
                if i[0] == addy:
                    existflag == True
            if not existflag:
                addys.append([addy, name, symbol])
        except:
            bot.say("Can't find this piece of trash")
            return
    else:
        existflag = False
        for i in addys:
            if addy == i[1] or addy == i[2]:
                addy = i[0]
                existflag = True
        if not existflag:
            bot.say("Can't find {}".format(addy))
            return
        try:
            r = requests.get("https://api.ethplorer.io/getTokenInfo/{}?apiKey=freekey".format(addy))
            j = r.json()
            name = j["name"]
            symbol = j["symbol"]
            holders = j["holdersCount"]
            price = j["price"]["rate"]
            mcap = j["price"]["marketCapUsd"]
            vol = j["price"]["volume24h"]
            bot.say("{} ({}) last price ${:.2f} on {:.2e} vol. Marketcap is ${:.2e} with {:.0f} addresses holding.".format(name, symbol, price, vol, mcap, holders))
            existflag = False
            for i in addys:
                if i[0] == addy:
                    existflag == True
            if not existflag:
                addys.append([addy, name, symbol])
        except:
            bot.say("Can't find this piece of trash")
            return
    with open('addys.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(addys)

@sopel.module.commands('usd')
def usd(bot, trigger):
    try:
        r = requests.get(krakusd)
        j = r.json()
        bot.say("Monero price in USD = ${0:,.2f}".format(float(j['result']['XXMRZUSD']['c'][0])))
    except:
        bot.say("Failed to retrieve price.")


@sopel.module.commands('usdt')
def usdt(bot, trigger):
    try:
        r = requests.get(krakusdt)
        j = r.json()
        stringtosay = "Last USDT/USD trade at ${0:.4f} on {1:.2f} USD 24 h volume. Highest bid at ${2:.4f}".format(float(j['result']['USDTZUSD']['c'][0]), float(j['result']['USDTZUSD']['v'][0]), float(j['result']['USDTZUSD']['b'][0]))
        bot.say(stringtosay)
    except:
        bot.say("Error getting USDT/USD data")


@sopel.module.commands('xmrtall', 'xmr')
def xmrtall(bot, trigger):
    stringtosend = ''

    # Polo
    try:
        r=requests.get(polourl)
        j=r.json()
        xmr=j["BTC_XMR"]
        last=float(xmr['last'])
#       change=float(xmr['percentChange'])
        vol=float(xmr['baseVolume'])
        stringtosend += "Poloniex last: {0:.6f} BTC on {1:.2f} BTC volume | ".format(last, vol)
    except:
        bot.say("Something borked ¯\(º_o)/¯")

    # bfx
    try:
        r = requests.get(finexbtc)
        j = r.json()
        stringtosend += "Bitfinex last: {0:.6f} on {1:.2f} XMR volume | ".format(float(j['last_price']), float(j['volume']))
    except:
        bot.say("Something borked ʕノ•ᴥ•ʔノ ︵ ┻━┻")

    # Kraken
    try:
        r = requests.get(krakbtc)
        j = r.json()
        stringtosend += "Kraken last: {0:.6f} on {1:.2f} XMR volume | ".format(float(j['result']['XXMRXXBT']['c'][0]), float(j['result']['XXMRXXBT']['v'][1]))
    except:
        bot.say("Something borked ¤\( `⌂´ )/¤")

    # Binance
    try:
        r = requests.get(binanceurl)
        j = r.json()
        found = False
        for i in j:
            if i["symbol"] == "XMRBTC":
                last=float(i['lastPrice'])
                vol=float(i['volume'])
                stringtosend += ("Binance last: {0:.6f} on {1:.2f} BTC volume | ".format(last, vol*last))
                found = True
    except:
        bot.say("Borka borka ┌∩┐(◣_◢)┌∩┐")

    # Trex
#    geturl = trexurl+'xmr'
#    try:
#        r = requests.get(geturl)
#        j = r.json()
#        xmr=j['result'][0]
#        last=float(xmr['Last'])
#       change=((last/float(xmr['PrevDay']))-1)
#        vol=float(xmr['BaseVolume'])
#        stringtosend += "Bittrex last: {0:.6f} BTC on {1:.2f} BTC volume | ".format(last, vol)
#    except:
#        bot.say("Something borked -_-")

    #Finally... print to IRC
    bot.say(stringtosend[:-2])

