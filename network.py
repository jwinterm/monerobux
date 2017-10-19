import sopel.module
import requests
import re

networkurl = "http://node.xmrbackb.one:18081/getinfo"

@sopel.module.commands('fork', 'forkening')
def fork(bot, trigger):
  try:
    r=requests.get(networkurl)
    j=r.json()
  except Exception,e:
    pass
  try:
    height=j["height"]
    forkheight=1400000
    if forkheight > height:
      bot.say("The current block height is {0:,}. Fork height is {1:,}. {2:,} blocks to go, happening in approximately {3:.2f} hours.".format(height,forkheight,forkheight-height,(forkheight-height)/30.0))
    else:
      bot.say("I don't know when the next fork is.")
  except:
    bot.say("Something borked -_-")

@sopel.module.commands('network')
def network(bot, trigger):
  try:
    r=requests.get(networkurl)
    j=r.json()
  except Exception,e:
    pass
  try:
    height=j["height"]
    diff=j["difficulty"]
    hashrate=float(diff)/120
    bot.say("The current block height is {0:,}. Difficulty is {1:,}. Hashrate is {2:.2f} Mh/s.".format(height,diff,hashrate/1e6))
  except:
    bot.say("Something borked -_-")

@sopel.module.commands('btcmempool')
def btcmempool(bot, trigger):
  try:
    r=requests.get('https://blockchain.info/q/unconfirmedcount')
    bot.say("The current number of txs in Bitcoin's mempool is {0}".format(r.text))
  except:
    bot.say("Fuck you, and fuck Bitcoin too")

@sopel.module.commands('mempool')
def mempool(bot, trigger):
  try:
    # r=requests.get('http://node.moneroworld.com:18081/getinfo')
    r=requests.get('http://node.xmrbackb.one:18081/getinfo')
    j=r.json()
    bot.say("The current number of txs in Monero's mempool is {0}".format(j['tx_pool_size']))
  except:
    bot.say("Something borked o_O")

@sopel.module.commands('blocksize')
def blocksize(bot, trigger):
  try:
    r=requests.get('http://moneroblocks.info/stats/block-medians')
    size=re.search('&nbsp;<\/strong><\/div>\s*<div class=\"col-xs-2\">(\d*)', r.text) 
    bot.say("Median blocksize over last 200 blocks is {0} bytes".format(size.group(1)))
  except:
    bot.say("Bomething sorked 0_0")

@sopel.module.commands('b2x')
def b2x(bot, trigger):
  try: 
    r=requests.get('https://blockchain.info/latestblock')
    j=r.json()
    height=j['height']
    forkheight=494784
    blocks=forkheight-int(height)
    bot.say("Bitcoin S2X fork due to happen on block {}. Current block is {}. 10 min per block estimate gives {} min, or {:.2f} hour, or {:.2f} days.".format(forkheight, height, blocks*10, blocks*0.16666, blocks*0.006944))
  except:
    bot.say("Bitcoin sucks.")
