import sopel.module
import requests
import re
import time

# networkurl = "http://node.marty.cf:18019/getinfo"
# networkurl = "http://node.xmrbackb.one:18081/getinfo"
# networkurl = "http://opennode.minemonero.pro:18081/getinfo"
# networkurl = "http://node.xmr.pt:18081/getinfo"
networkurl = "http://node.supportxmr.com:18081/getinfo"

jsonurl = "http://node1.keepitmonero.com:18089/json_rpc"
headers = {
    'Content-Type': 'application/json',
}
requestdata = '{"jsonrpc":"2.0","id":"0","method":"get_last_block_header"}'

@sopel.module.commands('fork', 'forkening')
def fork(bot, trigger):
  try:
    r=requests.get(networkurl)
    j=r.json()
  except Exception as e:
    pass
  try:
    height=j["height"]
    forkheight=2210000
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
  except:
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
    r=requests.get(networkurl)
    j=r.json()
    bot.say("The current number of txs in Monero's mempool is {0}".format(j['tx_pool_size']))
  except:
    bot.say("Something borked o_O")
    
@sopel.module.commands('lastblock')
def lastblock(bot, trigger):
  #try:    
  #  r=requests.get(lastblock)
    r=requests.post(jsonurl, headers=headers, data=requestdata)
    j=r.json()
    block=j['result']['block_header']
    bot.say("Last block found {0:.2f} minutes ago with height {1} included {2} transactions".format((time.time() - float(block['timestamp']))/60, block['height'], block['num_txes']))
  #except:
  #  bot.say("Something borked o_O")

@sopel.module.commands('blocksize')
def blocksize(bot, trigger):
  try:
    r=requests.get('http://moneroblocks.info/stats/block-medians')
    size=re.search('&nbsp;<\/strong><\/div>\s*<div class=\"col-xs-2\">(\d*)', r.text) 
    bot.say("Median blocksize over last 200 blocks is {0} bytes".format(size.group(1)))
  except:
    bot.say("Bomething sorked 0_0")

@sopel.module.commands('mine')
def mine(bot, trigger):
  try: 
    r=requests.get('https://supportxmr.com/api/network/stats')
    j=r.json()
    diff=float(j['difficulty'])
    value=float(j['value'])/1e12
    hashrate=float(trigger.group(2))
    xmrperday=(hashrate/(diff/120))*720*value
    bot.say("At {:.0f} h/s with network diff of {:.2e} and block reward {:.2f} you can expect {:.4f} XMR per day.".format(hashrate, diff, value, xmrperday))
  except:
    bot.say("Mining is for suckers.")

@sopel.module.commands('solo')
def solo(bot, trigger):
  try: 
    r=requests.get('https://supportxmr.com/api/network/stats')
    j=r.json()
    diff=float(j['difficulty'])
    hashrate=float(trigger.group(2))
    timetoblock=(diff/hashrate)
    bot.say("At {:.0f} h/s with network diff of {:.2e} your expected time for find a block is {:.2e} s or {:.2f} days.".format(hashrate, diff, timetoblock, timetoblock/(60*60*24)))
  except:
    bot.say("Mining is for suckers.")

@sopel.module.commands('b2x')
def b2x(bot, trigger):
  bot.say("Fuck off \\x")

def get_pools(coin = 'monero'):
  resp = requests.get("https://data.miningpoolstats.stream/data/time")
  time = int(resp.text)
  resp = requests.get("https://data.miningpoolstats.stream/data/{}.js?t={}".format(coin, time))
  j = resp.json()
  return j
@sopel.module.commands('miners')
def print_monero_miners_counter(bot, trigger):
  pools = get_pools()
  result = {
    'website counter': pools['poolsminers'],
    'website counter recalculated': sum([
        e['miners'] if ('miners' in e and isinstance(e['miners'], int) and e['miners'] >= 0) else (
            e['workers'] if ('workers' in e and isinstance(e['workers'], int) and e['workers'] >= 0) else (
                0
              )
          )
        for e in pools['data']
      ]),
    'count(miners) where miners >= 0': sum([e['miners'] for e in pools['data'] if 'miners' in e and isinstance(e['miners'], int) and e['miners'] > 0]),
    'count(workers) where workers >= 0': sum([e['workers'] for e in pools['data'] if 'workers' in e and isinstance(e['workers'], int) and e['workers'] > 0]),
    }
  bot.say(result)
