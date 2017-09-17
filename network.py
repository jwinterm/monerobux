import sopel.module
import requests
import re

networkurl = "http://api.minexmr.com:8080/stats"

@sopel.module.commands('fork', 'forkening')
def fork(bot, trigger):
  try:
    r=requests.get(networkurl)
    j=r.json()
  except Exception,e:
    pass
  try:
    height=j["network"]["height"]
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
    height=j["network"]["height"]
    diff=j["network"]["difficulty"]
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
