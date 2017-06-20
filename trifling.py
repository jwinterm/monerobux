# -*- coding: utf-8 -*-
import sopel.module
import random
import re
import requests
import praw
from client import *

@sopel.module.commands('4matter')
def fourmatter(bot, trigger):
    bot.say('Irish I be fookin <3 Milo')

@sopel.module.commands('aminorex')
def aminorex(bot, trigger):
    bot.say('if i could replace my wife with a robot...  i might seriously think about it')

@sopel.module.commands('ayylmao', 'lmao')
def lmao(bot, trigger):
    bot.say('https://i.redd.it/jjiwl9dbejoy.jpg')

@sopel.module.commands('banana')
def banana(bot, trigger):
    bot.say('(')

@sopel.module.commands('bananas')
def bananas(bot, trigger):
    bot.say('(((')

@sopel.module.commands('barolo')
def barolo(bot, trigger):
    bot.say('I just opened a 2004 barolo in your and all the devs honor -- https://i.ytimg.com/vi/-JvdfsIeb-s/hqdefault.jpg')

@sopel.module.commands('bear')
def bear(bot, trigger):
    bot.say(u'ʕ ·(エ)· ʔ'.encode('utf8'))

@sopel.module.commands('brothers')
def brothers(bot, trigger):
    bot.say(u'http://www.trollaxor.com/2011/11/brief-history-of-ascii-penis.html'.encode('utf8'))

@sopel.module.commands('buyorsell')
def buyorsell(bot, trigger):
    draw = random.random()
    if draw < 0.33:
        silly_string = "Sell, sell, sell!"  
    elif 0.66 > draw >= 0.33:
        silly_string = "Hodl!"  
    elif 1 > draw >= 0.66:
        silly_string = "Buy, buy, buy!"  
    bot.say(silly_string)

@sopel.module.commands('china')
def china(bot, trigger):
    bot.say('https://www.youtube.com/watch?v=RbM2F-cfN0A')

@sopel.module.commands('cursive')
def cursive(bot, trigger):
    instring = trigger.group(2)
    outstring = u''
    normals = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 
    curses  = [u'𝓪',u'𝓫',u'𝓬',u'𝓭',u'𝓮',u'𝓯',u'𝓰',u'𝓱',u'𝓲',u'𝓳',u'𝓴',u'𝓵',u'𝓶',u'𝓷',u'𝓸',u'𝓹',u'𝓺',u'𝓻',u'𝓼',u'𝓽',u'𝓾',u'𝓿',u'𝔀',u'𝔁',u'𝔂',u'𝔃',u'𝓐',u'𝓑',u'𝓒',u'𝓓',u'𝓔',u'𝓕',u'𝓖',u'𝓗',u'𝓘',u'𝓙',u'𝓚',u'𝓛',u'𝓜',u'𝓝',u'𝓞',u'𝓟',u'𝓠',u'𝓡',u'𝓢',u'𝓣',u'𝓤',u'𝓥',u'𝓦',u'𝓧',u'𝓨',u'𝓩']
    for idx, val in enumerate(instring):
        if val in normals:
            outstring += curses[normals.index(val)]
        else:
            outstring += val
    bot.say(outstring) 

@sopel.module.commands('dash')
def dash(bot, trigger):
    bot.say('http://www.dash-wash.com/it-it')

@sopel.module.commands('dealwithit')
def dealwithit(bot, trigger):
    bot.say(u'(•_•)   ( •_•)>⌐■-■    (⌐■_■)'.encode('utf8'))

@sopel.module.commands('disapprove')
def disapprove(bot, trigger):
    bot.say(u'ಠ_ಠ'.encode('utf8'))

@sopel.module.commands('ded')
def ded(bot, trigger):
    if random.random() < 0.5:
        bot.say('http://i3.kym-cdn.com/photos/images/original/000/715/140/3b2.jpg')
    else:
        bot.say('https://imgur.com/a/yzNZW')

@sopel.module.commands('donate', 'donation')
def donate(bot, trigger):
    bot.say('45SkxgDmcLmW5ByS7w9AG78JuJRvCoVKCdGJWnd4US95CBUAtvdGAdM2oHgZgTGjkEAUcwdqcryM819aqdeiKxHSQC8HkmS', trigger.nick)

@sopel.module.commands('dump')
def dump(bot, trigger):
    bot.say('https://www.youtube.com/watch?v=RHg8qIKJo1I')

@sopel.module.commands('eth')
def eth(bot, trigger):
    bot.say(u'The world computer 💻🌐'.encode('utf8'))

@sopel.module.commands('fib', 'fibonacci')
def fib(bot, trigger):
    bot.say(u'Pardon me, do you have a moment to discuss our lord and savior ✞Cheesus Monero✞?'.encode('utf8'))

@sopel.module.commands('flip')
def flip(bot, trigger):
    bot.say(u'(╯°□°）╯︵ ┻━┻'.encode('utf8'))

@sopel.module.commands('fuck')
def fuck(bot, trigger):
    bot.say("Fuck your {} if you want fuck!".format(trigger.group(2)))

fuckyouoptions = [
"http://imgur.com/Kt8os8v",
"https://pbs.twimg.com/profile_images/502111486915788801/DtB5ruDz_400x400.jpeg",
"http://s2.quickmeme.com/img/70/7073ff0ce9c54f6672f157ebef668c1b6bb123d15fc2e2bc062ec1558f964820.jpg",
"http://static.deathandtaxesmag.com/uploads/2015/01/staff-troll-fuck-you.png",
]
@sopel.module.commands('fuckyou')
def fuckyou(bot, trigger):
    bot.say(random.choice(fuckyouoptions))

@sopel.module.commands('gay')
def gay(bot, trigger):
    bot.say('https://i.imgur.com/RHbXrLa.png')

@sopel.module.commands('gui')
def gui(bot, trigger):
    bot.say('http://imgur.com/a/hnxfS')

@sopel.module.commands('hmm', 'hmmm')
def hmm(bot, trigger):
    # try:
        sub=reddit.subreddit('hmmm')
        posts=sub.new(limit=100)
        n=random.randint(0,100)
        for i, post in enumerate(posts):
            if i==n:
                bot.say(post.url)
    # except:
    #     bot.say("Something something reddit's servers")

@sopel.module.commands('isittrue')
def isittrue(bot, trigger):
    draw = random.random()
    if draw < 0.33:
        silly_string = "True as the day is long."  
    elif 0.66 > draw >= 0.33:
        silly_string = "Irrelevant question in this post-truth world."  
    elif 1 > draw >= 0.66:
        silly_string = "Lies! Damn Lies! It's statitistics!"  
    bot.say(silly_string)

@sopel.module.commands('jaxx')
def jaxx(bot, trigger):
    bot.say(u'This command will be implemented soon. Honest. Especially if the devs can provide some unpaid assistance. Soon™...')

@sopel.module.commands('joshua1234')
def joshua(bot, trigger):
    bot.say(u'The first, second, third, and fourth amongst joshes.')

@sopel.module.commands('jwinterm')
def jwinterm(bot, trigger):
    bot.say(u'j_winter_m')

@sopel.module.commands('kid', 'rehrar')
def kid(bot, trigger):
    bot.say(u'What up kid?')

@sopel.module.commands('lenny')
def lenny(bot, trigger):
    bot.say(u'( ͡° ͜ʖ ͡°)'.encode('utf8'))

@sopel.module.commands('ltc', 'chikun')
def ltc(bot, trigger):
    bot.say(u'🐔🐔🐔 https://cdn.meme.am/cache/instances/folder100/48222100.jpg 🐔🐔🐔'.encode('utf8'))

@sopel.module.commands('masternode', 'masternodes')
def masternode(bot, trigger):
    bot.say('http://hadoopilluminated.com/hadoop_illuminated/images/hdfs3.jpg')

@sopel.module.commands('moon')
def moon(bot, trigger):
    bot.say(u'┗(°0°)┛'.encode('utf8'))

@sopel.module.commands('multisig')
def multisig(bot, trigger):
    bot.say(u'𝓼𝓲𝓰𝓷𝓪𝓽𝓾𝓻𝓮 𝓼𝓲𝓰𝓷𝓪𝓽𝓾𝓻𝓮'.encode('utf8'))

@sopel.module.commands('nomnomnom')
def nomnomnom(bot, trigger):
    bot.say(u'ᗧ•••ᗣ'.encode('utf8'))

@sopel.module.commands('noom')
def noom(bot, trigger):
    bot.say(u'┏(.0.)┓'.encode('utf8'))

odboptions = [
"FBI don't you be watching me",
"Ooo baby I like it raw",
"Jacques Cousteau could never get this low"
]
@sopel.module.commands('odb', 'oldirty')
def odb(bot, trigger):
    bot.say(random.choice(confirmoptions))

perooptions = [
'https://www.youtube.com/watch?v=QqreRufrkxM',
'https://www.youtube.com/watch?v=ZnPrtiLy0uU'
]
@sopel.module.commands('pero')
def pero(bot, trigger):
    bot.say(random.choice(perooptions))

@sopel.module.commands('pivx')
def pivc(bot, trigger):
    bot.say("Masternodes + PoS...what could possibly go wrong?")

confirmoptions = [
"I can confirm that it is true",
"This is true",
"Fake news",
"Alternative fact",
"The outlook is murky, ask again later"
]
@sopel.module.commands('pleaseconfirm', 'confirm')
def confirm(bot, trigger):
    bot.say(random.choice(confirmoptions))

@sopel.module.commands('rarepepe', 'rare')
def rarepepe(bot, trigger):
    try:
        r=requests.get('https://rarepepewallet.com/feed')
        j=r.json()
    except:
        bot.say("Problem getting rarepepe data :sadfrogface:")
    try:
        if trigger.group(2) == None:
            name=random.choice(j.keys())
        else:
            name=trigger.group(2).upper()
        pepe=j[name]
        bot.say("{0} is the #{1} card in series {2} of which {3} exist {4}".format(name, pepe['order'], pepe['series'], pepe['quantity'], pepe['img_url'].replace('\\', '')))
    except:
        bot.say("{0} rare pepe doesn't seem to exist".format(trigger.group(2)))
        

@sopel.module.commands('rip')
def rip(bot, trigger):
    bot.say(u'(X_X) ☜ (◉▂◉ ) we hardly knew ye'.encode('utf8'))

@sopel.module.commands('romerito', 'romero')
def romerito(bot, trigger):
    draw = random.random()
    if draw < 0.25:
        silly_string = "O Romerito, Romerito! wherefore art thou Romerito?"  
    elif 0.5 > draw >= 0.25:
        silly_string = "To buy or not to buy: that is the question"  
    elif 0.75 > draw >= 0.5:
        silly_string = "Cowards die many times before their deaths; the Romerito never taste of death"  
    elif 1 > draw >= 0.75:
        silly_string = "Et tu, Romerito!"  
    bot.say(silly_string)

@sopel.module.commands('scam')
def scam(bot, trigger):
    bot.say(u'http://i.imgflip.com/is8.jpg')

@sopel.module.commands('soon')
def soon(bot, trigger):
    bot.say(u'Two weeks™'.encode('utf8'))

@sopel.module.commands('shrug')
def shrug(bot, trigger):
    bot.say(u'¯\_(ツ)_/¯'.encode('utf8'))

@sopel.module.commands('summon')
def summon(bot, trigger):
    if trigger.group(2) == None:
        bot.say("{0} has summoned...no one".format(trigger.nick))
    else:
        try:
            trigger.group(2).decode('ascii')
            bot.say("{0} has summoned {1}, ༼つ ◕_◕ ༽つ come to us {1} ༼つ ◕_◕ ༽つ".format(trigger.nick, trigger.group(2)))
        except:
            bot.say("Stop using non-ascii characters! (╯°□°）╯︵ ( . 0 .)")

@sopel.module.commands('timetravelpp')
def timetravelpp(bot, trigger):
    bot.say("A journey is best measured in pepes, rather than miles http://rarepepedirectory.com/wp-content/uploads/2016/09/timetravelpepe.jpg")

reddit=praw.Reddit(client_id=client_id, 
                   client_secret=client_secret, 
                   user_agent='monerobux',
                   username=username,
                   password=password)
@sopel.module.commands('tinytrump')
def tinytrump(bot, trigger):
    try:
        sub=reddit.subreddit('tinytrump')
        posts=sub.new(limit=100)
        n=random.randint(0,100)
        for i, post in enumerate(posts):
            if i==n:
                bot.say(post.url)
    except:
        bot.say("Something something reddit's servers")

@sopel.module.commands('trump')
def trump(bot, trigger):
    bot.say("Monero is the best crypto, believe me, I know crypto and it's going to be yuuuuuuuge!")

@sopel.module.commands('tumbleweed')
def trump(bot, trigger):
    bot.say("https://rootco.de/2016-03-28-why-use-tumbleweed/")

@sopel.module.commands('unflip')
def unflip(bot, trigger):
    bot.say(u'┬─┬ノ( º _ ºノ)'.encode('utf8'))

urmomoptions = [
"ur mom is so stupid she bought all the dash",  
"ur momma got a peg leg with a kickstand",
"ur mom is so fat it looks like she's just gliding across the floor",  
"your mother is so obese she would have mass whether or not the Higgs boson exists",  
"ur mom is so fat that her blood type is nutella",  
"ur mama is so fat she wears neck deoderant",  
"ur mom's middle name is Mudbone",  
"ur momma has a glass eye with a fish in it",  
"ur mama is so stupid she sold her romero for bitcoins",  
"ur momma look like a Simpsons character",
"ur mom is so ugly Donald Trump wouldn't even grab her by the pussy",
"ur momma is so stupid she listens to rpietila",
"ur mom is Amanda B Johnson",
"US ur mom if u want to U!",
"ur mom is so stupid she thinks Craig Wright is Satoshi"
]  
@sopel.module.commands('urmom', 'yourmom', 'yomom', 'yomomma')
def urmom(bot, trigger):
    bot.say(random.choice(urmomoptions))

vitalikoptions = [
"https://pbs.twimg.com/media/CrWjczJXgAExF2S.jpg",
"mETH, not even once: https://cdn-az.allevents.in/banners/e7df519e0808bac49fa3aaf503aff87d",
"Betteridge's law of headlines: https://fortunedotcom.files.wordpress.com/2016/09/blo_startups_2520x1667.png"
]
@sopel.module.commands('vitalik', 'buterin')
def vitalik(bot, trigger):
    bot.say(random.choice(vitalikoptions))


@sopel.module.commands('wat')
def wat(bot, trigger):
    bot.say("https://www.destroyallsoftware.com/talks/wat")

zcashoptions = [
"Trust us guys, we totally smashed that computer up, with like...magnetic baseball bats.", 
"https://youtu.be/A51Bl3jkF0c"
]
@sopel.module.commands('zec', 'zcash')
def zcash(bot, trigger):
    bot.say(random.choice(zcashoptions))

@sopel.module.rule('monerobux o\/')
def wave(bot, trigger):
    #bot.reply(u'‹^› ‹(•_•)› ‹^›'.encode('utf8'))
    bot.reply('hello')
#@sopel.module.rule('[Tt]rump')
#def politics(bot, trigger):
#    bot.reply("politics is the mind killer")

@sopel.module.commands('asp')
def asp(bot, trigger):
    polourl = "https://poloniex.com/public?command=returnTicker"
    stampurl = 'https://www.bitstamp.net/api/ticker/'
    cmcurl = "https://api.coinmarketcap.com/v1/ticker/monero/"
    trexurl = "https://bittrex.com/api/v1.1/public/getmarketsummary?market=btc-ans"

    try:
        r=requests.get(cmcurl)
        j=r.json()
        xmrbtc_price=float(j[0]['price_btc'])
    except:
        bot.say("Error connecting to CoinMarketCap")
    try:
        r = requests.get(trexurl)
        j = r.json()
        ans=j['result'][0]
        last=float(ans['Last'])    
        value_ans = float(last*231.6)
    except:
        print ("Error retrieving data from Bittrex")    
    try:
        r=requests.get(polourl)
        j=r.json()
    except:
        bot.say("Error connecting to Poloniex")
            
    label_dash="BTC_DASH"
    label_decred="BTC_DCR"
    label_factom="BTC_FCT"
    label_golem="BTC_GNT"
    label_maidsafecoin="BTC_MAID"
    label_augur="BTC_REP"
    label_stellar="BTC_STR"
    label_nem="BTC_XEM"
    label_ripple="BTC_XRP"
    label_zcash="BTC_ZEC"
    label_nxt="BTC_NXT"
    label_sia="BTC_SC"
    label_dgb="BTC_DGB"
    label_sys="BTC_SYS"
    
    # Bitstamp
    try: 
        stampresult = requests.get(stampurl)
        stampjson = stampresult.json()
    except:
        stampjson = False
    if stampjson:
        stamp_price = float(stampjson['last'])
    # Poloniex  
    try:
        ticker_dash=j[label_dash]
        ticker_decred=j[label_decred]
        ticker_factom=j[label_factom]
        ticker_golem=j[label_golem]
        ticker_maidsafecoin=j[label_maidsafecoin]
        ticker_augur=j[label_augur]
        ticker_stellar=j[label_stellar]
        ticker_nem=j[label_nem]
        ticker_ripple=j[label_ripple]
        ticker_zcash=j[label_zcash]
        ticker_nxt=j[label_nxt]
        ticker_sia=j[label_sia]
        ticker_dgb=j[label_dgb]
        ticker_sys=j[label_sys]  
        last_dash=float(ticker_dash['last'])
        last_decred=float(ticker_decred['last'])
        last_factom=float(ticker_factom['last'])
        last_golem=float(ticker_golem['last'])
        last_maidsafecoin=float(ticker_maidsafecoin['last'])
        last_augur=float(ticker_augur['last'])
        last_stellar=float(ticker_stellar['last'])
        last_nem=float(ticker_nem['last'])
        last_ripple=float(ticker_ripple['last'])
        last_zcash=float(ticker_zcash['last'])
        last_nxt=float(ticker_nxt['last'])
        last_sia=float(ticker_sia['last'])
        last_dgb=float(ticker_dgb['last'])
        last_sys=float(ticker_sys['last'])      
        value_dash = float(last_dash*18.84760476)
        value_decred = float(last_decred*93.74095377)
        value_factom = float(last_factom*207.78912373)
        value_golem = float(last_golem*7374.44608569)
        value_maidsafecoin = float(last_maidsafecoin*5973.05389222)
        value_augur = float(last_augur*94.01892768)
        value_stellar = float(last_stellar*318974.81202454)
        value_stellar_h = float(8.34800202)
        value_nem = float(last_nem*29892.11866946)
        value_ripple = float(last_ripple*27962.37965895)
        value_ripple_h = float(3.17485452)
        value_zcash = float(last_zcash*16.47649534)
        value_nxt = float(last_nxt*14932.63473053)
        value_sia = float(last_sia*129377.43190662)
        value_dgb = float(last_dgb*84177.21518989)
        value_sys = float(last_sys*10523.26194748)

        total = value_dash + value_decred  + value_factom + value_golem + value_maidsafecoin + value_augur + value_stellar + value_nem + value_ripple + value_zcash
        total_june = value_nxt + value_sia + value_dgb + value_sys + value_ans        
        xmr_totalvalue = float(total / xmrbtc_price)
        asppercent = ((((stamp_price * total) / 14950)-1)*100) + ((((stamp_price * total_june) / 13240)-1)*100)
        if asppercent >= 0: 
            aspsign = '+'
        else:
            aspsign = '-'
        xmrpercent = ((((650*(xmrbtc_price*stamp_price)/14950)-1)*100))  + (((250*(xmrbtc_price*stamp_price)/13240)-1)*100)
        if xmrpercent >= 0: 
            xmrsign = '+'
        else:
            xmrsign = '-'  

        bot.say("{0} {1:.2f}BTC; {2} {3:.2f}BTC; {4} {5:.2f}BTC; {6} {7:.2f}BTC; {8} {9:.2f}BTC; {10} {11:.2f}BTC; {12} {13:.2f}[{14:.2f}]BTC; {15} {16:.2f}BTC; {17} {18:.2f}[{19:.2f}]BTC; {20} {21:.2f}BTC; {22} {23:.2f}BTC; {24} {25:.2f}BTC; {26} {27:.2f}BTC; {28} {29:.2f}BTC; {30} {31:.2f}BTC; ASP Total:{32:.2f}BTC/{33:,.0f}USD/{34:,.1f}XMR (02-May+20-Jun outlay, 10BTC+5BTC/14,950USD+13,240USD/650XMR+250XMR) (Since begin ASP:{35}{36:.2f}% XMR:{37}{38:.2f}%, Harvested 11.52BTC)".format("DASH", value_dash, "DCR", value_decred, "FCT", value_factom, "GNT", value_golem, "MAID", value_maidsafecoin, "REP", value_augur, "STR", value_stellar, value_stellar_h, "XEM", value_nem, "XRP", value_ripple, value_ripple_h, "ZEC", value_zcash, "NXT", value_nxt, "SIA", value_sia, "DGB", value_dgb, "SYS", value_sys, "ANS", value_ans, total+total_june, stamp_price * (total + total_june), xmr_totalvalue, aspsign, asppercent, xmrsign, xmrpercent))
    except:
        bot.say("ERROR!")
