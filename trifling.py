# -*- coding: utf-8 -*-
import sopel.module
import random
import re
import requests
import praw
import client
from threading import Timer
from html.parser import HTMLParser

@sopel.module.commands('4matter')
def fourmatter(bot, trigger):
    bot.say('Irish I be fookin <3 Milo')

@sopel.module.commands('allah')
def allah(bot, trigger):
    bot.say('allah is doing')
    bot.say('sun is not doing allah is doing')
    bot.say('to accept Islam say that i bear witness that there is no deity worthy of worship except Allah and Muhammad peace be upon him is his slave and messenger')

@sopel.module.commands('_.')
def faceflip(bot, trigger):
    bot.say(':/   :|   :\   .¯.   /:   |:   \:   ._.   :/   :|   :\   .¯.   /:   |:   \:   ._.')
   
@sopel.module.commands('ada', 'hoskinson')
def ada(bot, trigger):
    bot.say('DO YOU KNOW WHO I AM?')

@sopel.module.commands('aids')
def aids(bot, trigger):
    bot.say('https://youtu.be/8iZcGnz7WcI?t=59')

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

@sopel.module.commands('bb')
def bb(bot, trigger):
    bot.say('https://www.youtube.com/watch?v=_VvbP0QNmF0')

bbloptions = [
"don't worry",
"it's fine",
"everything is good",
"😇🤣",
"afk",
"it's all good",
"please go back and re-read it, it's good",
"don't worry about me, I'm relaxed for a reason",
"I will be back expectedly an hr or more later",
"you didn't understand what you read, I'll be back later",
"pls wait for a little",
".....ok I'm back",
"actual bbl",
"Then you need to review it again. Take it from the author who apparently knows what he's talking about. Otherwise just ignore it and pretend I didn't post it OK, bbl",
"As a matter of fact it sounds like you have an actually understood or read all of the details yet so I will give you some more timei, bbl"
]
@sopel.module.commands('bbl')
def bbl(bot, trigger):
    bot.say(random.choice(bbloptions))

@sopel.module.commands('bear')
def bear(bot, trigger):
    bot.say(u'ʕ ·(エ)· ʔ')

@sopel.module.commands('billions')
def billions(bot, trigger):
    bot.say('https://www.youtube.com/watch?v=u_aLESDql1U')

@sopel.module.commands('brothers')
def brothers(bot, trigger):
    bot.say(u'http://www.trollaxor.com/2011/11/brief-history-of-ascii-penis.html')

@sopel.module.commands('bp', 'bps', 'bulletproof', 'bulletproofs')
def bulletproofs(bot, trigger):
    bot.say(u'https://www.youtube.com/watch?v=Kk8eJh4i8Lo')

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

@sopel.module.commands('chad')
def chad(bot, trigger):
      bot.say('https://i.redd.it/6pvmtwkoy0a21.jpg')

@sopel.module.commands('cheerup')
def cheerup(bot, trigger):
      bot.say('https://www.youtube.com/watch?v=NXfC16rv_fs')

@sopel.module.commands('china')
def china(bot, trigger):
    bot.say('https://youtu.be/ZrNrleD2ZFs')

@sopel.module.commands('collect')
def collect(bot, trigger):
    syntax_err_msg = 'The syntax is: .collect <what> <quantity>'

    # check for too many args
    if trigger.group(5):
        bot.say('Too many arguments!  ' + syntax_err_msg)
        return

    # check for enough args
    if not trigger.group(4):
        bot.say('Too few arguments!  ' + syntax_err_msg)
        return

    # make sure second arg is a number
    try:
        float(trigger.group(4))
    except:
        bot.say('Second arg must be a number!  ' + syntax_err_msg)
        return

    item = str(trigger.group(3)).lower()
    quantity = float(trigger.group(4))

    # the values must be ints or floats
    Prices = { \
        "bottle": .05, "bottles": .05, \
        "can": .03, "cans": .03 \
    }

    # check if we know the value for the item
    if item in Prices:
        pass
    else:
        bot.say(item + "!?!  I don't know the value!")
        return

    coin = "monero"
    coin_price = 0

    # try to get the USD, first from gecko
    try:
        r = requests.get('https://api.coingecko.com/api/v3/coins/' + coin)
        j = r.json()
        coin_price = j['market_data']['current_price']['usd']
    except:
        # try once more before giving up
        try:
            r=requests.get('https://api.coinmarketcap.com/v1/ticker/' + coin)
            j=r.json()
            coin_price=float(j[0]['price_usd'])
        except:
            bot.say("Failed to retrieve price for {}.".format(coin))
            return

    if coin_price == 0:
        # this should never execute, right?
        bot.say("{} is worth nothing.".format(coin))
        return
    else:
        value_of_one_item = 0

        try:
            value_of_one_item = float(Prices.get(item))
        except:
            # the values in Prices must be ints or floats, of course
            bot.say("Couldn't convert item value to a float!  How?!?  Why?!?")
            return

        value_of_items_collected_in_one_day = quantity * value_of_one_item
        weekly_coins_to_buy = value_of_items_collected_in_one_day * 7 / coin_price

        bot.say('{0} price: ${1:,.2f}, and {2} price: ${3:,.2f}'.format(item.capitalize(), value_of_one_item, coin.capitalize(), coin_price))
        bot.say('{0}: collect {1} per day to exchange for {2:,.5f} {3} each week!'.format(item.capitalize(), quantity, weekly_coins_to_buy, coin))

@sopel.module.commands('covid', 'corona', 'conv')
def covid(bot, trigger):
    if not trigger.group(2):
        try:
            r = requests.get(
                'https://corona.lmao.ninja/v2/all')
            j = r.json()
            cases = j['cases']
            deaths = j['deaths']
            recovered = j['recovered']
            active = j['active']
            affectedCountries = j['affectedCountries']
            bot.say("Total Cases : {0} || Total Deaths : {1} || Recovered Cases : {2} || Active Cases : {3} || Affected Countries : {4} ".format(
                cases, deaths, recovered, active, affectedCountries))
        except:
            bot.say("API fucked up :(")
    else:
        try:
            countryname = trigger.group(2)
            r = requests.get(
                'https://corona.lmao.ninja/v2/countries/{0}'.format(countryname))
            j = r.json()
            country = j['country']
            cases = j['cases']
            todayCases = j['todayCases']
            deaths = j['deaths']
            todayDeaths = j['todayDeaths']
            recovered = j['recovered']
            active = j['active']
            critical = j['critical']
            bot.say("Country : {0} || Total Cases : {1} || Today Cases : {2} || Total Deaths : {3} || Today Deaths : {4} || Recovered Cases : {5} || Active Cases : {6} || Cricital Cases : {7} ".format(
                country, cases, todayCases, deaths, todayDeaths, recovered, active, critical))
        except:
            bot.say("API fucked up :(")

@sopel.module.commands('cryptosid', 'sid')
def cryptosid(bot, trigger):
    bot.say('https://img.huffingtonpost.com/asset/58acbbd0280000d59899a57a.jpeg?ops=crop_5_33_460_393,scalefit_720_noupscale')

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
    bot.say(u'(•_•)   ( •_•)>⌐■-■    (⌐■_■)')

@sopel.module.commands('Deathtobitcoin', 'Deathtobitcoin2')
def deathtobitcoin2(bot, trigger):
    bot.say('Devs, moderators, whoever you fucking are, please put my money back with interest. Or make my money appear in my wallet with interest!')

@sopel.module.commands('diiorio')
def diiorio(bot, trigger):
    bot.say(u'http://www.contravex.com/2016/06/29/from-the-scammer-files-anthony-di-iorio/')

@sopel.module.commands('disapprove')
def disapprove(bot, trigger):
    bot.say(u'ಠ_ಠ')

@sopel.module.commands('ded')
def ded(bot, trigger):
    if random.random() < 0.5:
        bot.say('http://i3.kym-cdn.com/photos/images/original/000/715/140/3b2.jpg')
    else:
        bot.say('https://imgur.com/a/yzNZW')

@sopel.module.commands('donate', 'donation')
def donate(bot, trigger):
    bot.say('XMR: 848bZGkKWNwi588P5EN3cwE7n8UZtCWYVQ3ppWutYkSj6ihLQRawivEgdj6AddpDZ9eCZEr5B6kpih3U2vQzhpPnRhNkfut', trigger.nick)
    bot.say('BTC: 38JoVcr49qKZTfweNKDkZSmPYdGu86AYqr', trigger.nick)

@sopel.module.commands('dump')
def dump(bot, trigger):
    bot.say('https://www.youtube.com/watch?v=RHg8qIKJo1I')

@sopel.module.commands('encrypt')
def encrypt(bot, trigger):
    bot.say("https doesn't hide the fact that i'm using https so that's why i don't use encryption because everyone is trying to crack encryption so i just don't use encryption because no one is looking at unencrypted data because everyone wants encrypted data to crack")

@sopel.module.commands('eth')
def eth(bot, trigger):
    bot.say(u'The world computer 💻🌐')

@sopel.module.commands('ferret', 'ferretinjapan')
def ferret(bot, trigger):
    bot.say(u'♥‿♥ https://crypto314.com/wp-content/uploads/2017/09/monero-1505185532555-723x1024.png ♥‿♥')

@sopel.module.commands('fib', 'fibonacci')
def fib(bot, trigger):
    bot.say(u'Pardon me, do you have a moment to discuss our lord and savior ✞Cheesus Monero✞?')

@sopel.module.commands('flip')
def flip(bot, trigger):
    bot.say(u'(╯°□°）╯︵ ┻━┻')

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

hitleroptions = [
'https://www.youtube.com/watch?v=L2WfedZG7bo',
r"There's always Aeon",
'http://adolfcoin.camp/'
]
@sopel.module.commands('hitler', 'adolf')
def hitler(bot, trigger):
    bot.say(random.choice(hitleroptions))

@sopel.module.commands('hmm', 'hmmm')
def hmm(bot, trigger):
    reddit = praw.Reddit(client_id=client.client_id, client_secret=client.client_secret, user_agent='asdfasdfasdfjhwrgth', username=client.username, password=client.password)

    #try:
    sub=reddit.subreddit('hmmm')
    posts=sub.new(limit=100)
    n=random.randint(0,100)
    for i, post in enumerate(posts):
        if i==n:
            bot.say(post.url)
    #except:
    #    bot.say("Something something reddit's servers")

herooptions = [
"https://video.twimg.com/tweet_video/DEnItJjV0AI81CK.mp4",
"https://media.giphy.com/media/REH3MZp1FeCM8/giphy.gif",
]
@sopel.module.commands('hero')
def hero(bot, trigger):
    bot.say(random.choice(herooptions))

@sopel.module.commands('hotline')
def hotline(bot, trigger):
    if random.random() > 0.3:
        bot.say(u'☎  Call 1-800-273-8255 to reach the National Suicide Prevention Lifeline ☎' .encode('utf8'))
    else:
        bot.say('http://pixel.nymag.com/imgs/daily/vulture/2015/10/20/drake-dance/drake-4.w529.h352.gif')

@sopel.module.commands('news')
def news(bot, trigger):
    bot.say("https://www.youtube.com/watch?v=Gr_WtFW0a8Y")

@sopel.module.commands('invest')
def invest(bot, trigger):
    bot.say('i think invest in bitcoin is much more safe and profitable because bitcoin price rising to higher value and we do not face to any risk when we invest our money in bitcoin and i if we invest our money in bitcoin we will be get a good profit from bitcoin in the future so i think bitcoin is much more profitable currency than altcoins.')

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

@sopel.module.commands('jimbell')
def jimbell(bot, trigger):
    if not trigger.group(2):
        bot.say(u'https://en.wikipedia.org/wiki/Jim_Bell')
    else:
        bot.say(u'{} has opened an assassination futures market predicting the impending demise of {}.'.format(trigger.nick, trigger.group(2)))

@sopel.module.commands('john_alan')
def joshua(bot, trigger):
    bot.say(u'Ps the coverage blackspot I reported 37 times in 2016/2017 is STILL DOWN. If I were running Virigin Mobile I’d be so ashamed of myself.')

@sopel.module.commands('jwinterm')
def jwinterm(bot, trigger):
    bot.say(u'j_winter_m')

@sopel.module.commands('kid', 'rehrar')
def kid(bot, trigger):
    bot.say(u'What up kid?')

@sopel.module.commands('koan')
def koan(bot, trigger):
    bot.say("The use cases are many and varied")

@sopel.module.commands('kramer')
def kramer(bot, trigger):
    bot.say("Waiting for a retrace to 0.007")

@sopel.module.commands('lambo')
def lambo(bot, trigger):
    bot.say(u'Our mission is to give you a taste of the lambo dream 🏎 ')

@sopel.module.commands('lietome')
def lietome(bot, trigger):
    bot.say(u'https://www.youtube.com/watch?v=R5AsQbLHWbw')

@sopel.module.commands('livermore')
def livermore(bot, trigger):
    bot.say(u'https://en.wikipedia.org/wiki/Reminiscences_of_a_Stock_Operator')

@sopel.module.commands('loki')
def loki(bot, trigger):
    bot.say(u'Only $13 to run a masternode 🤑🤡 https://i.imgur.com/aK5kiwi.png')

@sopel.module.commands('luigi')
def luigi(bot, trigger):
    bot.say(u'🍄 luigi is doing. mario is not doing luigi is doing 🍄')

@sopel.module.commands('ltc', 'chikun')
def ltc(bot, trigger):
    bot.say(u'🐔🐔🐔 https://cdn.meme.am/cache/instances/folder100/48222100.jpg 🐔🐔🐔')

@sopel.module.commands('major')
def major(bot, trigger):
    bot.say(r"Showed them a sneak peak of the MAJOR Monero announcement that is happening at tomorrow's meetup, they're excited!")

@sopel.module.commands('masternode', 'masternodes')
def masternode(bot, trigger):
    bot.say('http://hadoopilluminated.com/hadoop_illuminated/images/hdfs3.jpg')

@sopel.module.commands('monerov', 'v')
def monerov(bot, trigger):
    bot.say(u"🔒🔒🔒 MoneroV is more secured than others. That's why it is better invest on moneroV. 💰💰💰")

@sopel.module.commands('moon')
def moon(bot, trigger):
    bot.say(u'┗(°0°)┛')

@sopel.module.commands('multisig')
def multisig(bot, trigger):
    bot.say(u'𝓼𝓲𝓰𝓷𝓪𝓽𝓾𝓻𝓮 𝓼𝓲𝓰𝓷𝓪𝓽𝓾𝓻𝓮')

@sopel.module.commands('myriad', 'myr', 'myriadcoin')
def myriad(bot, trigger):
    bot.say(u'Myriad - A coin for everyone 🖐')

@sopel.module.commands('needmoney', 'needmoney90', 'nm90')
def needmoney(bot, trigger):
    bot.say(u'cash rules everything around me C.R.E.A.M get the money 💵 💵 bill yall')

@sopel.module.commands('nioc')
def nioc(bot, trigger):
    bot.say(u'https://ifunny.co/fun/laeIohx56')

@sopel.module.commands('nobody')
def nobody(bot, trigger):
    bot.say('https://www.youtube.com/watch?v=YA631bMT9g8')

@sopel.module.commands('nomnomnom', 'nomnom')
def nomnomnom(bot, trigger):
    bot.say(u'ᗧ•••ᗣ')

@sopel.module.commands('noom')
def noom(bot, trigger):
    bot.say(u'┏(.0.)┓')

@sopel.module.commands('notbad', 'dorian')
def notbad(bot, trigger):
    bot.say(u'（´ー｀） http://hackingdistributed.com/images/2014-01-01-bitcoin/dorian1.jpg （´ー｀）')

@sopel.module.commands('obama')
def obama(bot, trigger):
    bot.say('https://media0.giphy.com/media/9W4FM9Eis7Vyo/giphy.gif')

odboptions = [
"FBI don't you be watching me",
"Ooo baby I like it raw",
"Jacques Cousteau could never get this low"
]
@sopel.module.commands('odb', 'oldirty')
def odb(bot, trigger):
    bot.say(random.choice(odboptions))

@sopel.module.commands('orff')
def orff(bot, trigger):
    bot.say("O Fortuna velut luna statu variabilis, semper crescis aut decrescis; vita detestabilis nunc obdurat et tunc curat ludo mentis aciem, egestatem, potestatem dissolvit ut glaciem.")

@sopel.module.commands('pamp')
def pamp(bot, trigger):
    bot.say("Pamp o clock yet?")

perooptions = [
'https://www.youtube.com/watch?v=QqreRufrkxM',
'https://www.youtube.com/watch?v=ZnPrtiLy0uU',
'https://www.youtube.com/watch?v=d8qOV1z7ZA0'
]
@sopel.module.commands('pero')
def pero(bot, trigger):
    bot.say(random.choice(perooptions))

@sopel.module.commands('pivx')
def pivc(bot, trigger):
    bot.say("Masternodes + PoS...what could possibly go wrong?")

@sopel.module.commands('pony')
def pony(bot, trigger):
    bot.say("https://www.youtube.com/watch?v=O3rpmctmC_M")

@sopel.module.commands('primer')
def primer(bot, trigger):
    bot.say("The point is not how much i made, point is fluffy did this on purpose, more than 10 people were in on it. His commit access needs to be revoked asap!")

@sopel.module.commands('praise')
def praise(bot, trigger):
    bot.say("https://praisemonero.com")

@sopel.module.commands('pubg')
def pubg(bot, trigger):
    bot.say("https://i.redd.it/o6o5gqmetacz.jpg")

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

projectingoptions = [
"https://i.warosu.org/data/fa/img/0059/31/1365465556033.jpg",
"https://thenicessist.files.wordpress.com/2015/12/screen-shot-2015-12-15-at-8-03-04-pm.png?w=748",
"https://4.bp.blogspot.com/-cMYssGE9g6w/VNru-2E-bDI/AAAAAAAAA3Y/fM91wN757Z0/s1600/Projection.PNG",
"https://s-media-cache-ak0.pinimg.com/originals/b7/fa/f3/b7faf3aac68dc3f15d3526ecb292dc8b.jpg",
"https://s-media-cache-ak0.pinimg.com/originals/17/40/e1/1740e15f12c153c00a041d95978f831c.gif"
]
@sopel.module.commands('projecting')
def projecting(bot, trigger):
    bot.say(random.choice(projectingoptions))

@sopel.module.commands('purge')
def purge(bot, trigger):
    bot.say(u'♔♔♔ Bow to the king https://preview.redd.it/fr8q7x9utnzy.png?width=612&auto=webp&s=8bf7aa7674d2dc3157b776ae07771144833cd879  ♔♔♔')

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
    bot.say(u'(X_X) ☜ (◉▂◉ ) we hardly knew ye')

@sopel.module.commands('risto', 'rpietila')
def risto(bot, trigger):
    bot.say(u'Zionists own the media, including Hollywood. It is nothing extraordinary for them to use it to further their goals. Just see what they are propagating every day in every media outlet. And the compulsory disclaimer: Zionist != Jew. Zionists in my understanding are typically mostly not even ethnic Jews, and the supermajority of Jews certainly are not Zionists. Zionism is a purely political supremacy movement.')

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

@sopel.module.commands('rotten')
def rotten(bot, trigger):
    reddit = praw.Reddit(client_id=client.client_id, client_secret=client.client_secret, user_agent='asdfasdfasdfjhwrgth', username=client.username, password=client.password)
    try:
        sub=reddit.subreddit('4chan')
        posts=sub.hot(limit=100)
        n=random.randint(0,100)
        for i, post in enumerate(posts):
            if i==n:
                bot.say(post.url)
    except:
        bot.say("Something something reddit's servers")

@sopel.module.commands('ryo')
def ryo(bot, trigger):
    bot.say(u'https://i.imgflip.com/2nn22t.jpg')

sadminoptions = [
    u"Hi all i was setupping a mining pool and in trynd on virtual box (install It on PC make me Crazy with wifi driver...i really dont know how make them work) So...when i try run monerod said something like that an HDD Is too slow d'oro Sync and stops...but im on VM and a virtual box with NVME emulated dont LET me boot Ubuntu...",
    u"POOL ONLINE, ALL WORK AND FEE 0% i had problems",
    u"Im tryng fixing things",
    u"Idk why now pool say Can connect webui and stop work...in gonna recompile It...back in 30 minutes"
]
@sopel.module.commands('sadmin')
def sadmin(bot, trigger):
    bot.say(random.choice(sadminoptions))

@sopel.module.commands('scam')
def scam(bot, trigger):
    bot.say(u'http://i.imgflip.com/is8.jpg')

@sopel.module.commands('soon')
def soon(bot, trigger):
    bot.say(u'Two weeks™')

@sopel.module.commands('shillo', 'cid')
def shillo(bot, trigger):
    bot.say(u'☠☠☠ Crypto is ded https://i.kym-cdn.com/photos/images/original/001/321/553/f03.jpg ☠☠☠ ')

@sopel.module.commands('softich')
def softich(bot, trigger):
    bot.say(u'🐻🐻🐻 https://imgflip.com/i/1ve397 🐻🐻🐻')

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

suraeoptions = [
"you are speaking with such generalities, it's impossible to confirm or deny any of what you are saying, so i'll just nod and give you the benefit of the doubt and assume we are in agreement on something unspoken. haha",
"The Buddha, the Godhead, resides quite as comfortably in the circuits of a digital computer or the gears of a cycle transmission as he does at the top of the mountain, or in the petals of a flower. To think otherwise is to demean the Buddha - which is to demean oneself.",
"update coefList[k] = COEFPROD(coefList, q[j][k]). Can you spot a problem with that? The method signature of COEFPROD is scalar[] COEFPROD(scalar[] c, scalar[] d) <--- yeah, pass it coefList[k]."
]
@sopel.module.commands('surae')
def surae(bot, trigger):
    bot.say(random.choice(suraeoptions))

@sopel.module.commands('tech', 'initforthetech')
def tech(bot, trigger):
    bot.say("I'm in it for the tech https://i.imgur.com/h2g7wSe.png 👩‍💻⚙")

@sopel.module.commands('tether')
def chad(bot, trigger):
      bot.say("For downvoters: You are downvoting facts and truth, quite far from your scientific beliefs. Just read the actual whitepaper and then come and downvote. Don't repeat what you read or heard or think is obvious, obviously.")

@sopel.module.commands('thicc')
def thicc(bot, trigger):
    bot.say("https://pics.me.me/you-on-the-beach-and-luigi-walk-pass-and-give-42542268.png")

@sopel.module.commands('timetravelpp')
def timetravelpp(bot, trigger):
    bot.say("A journey is best measured in pepes, rather than miles http://rarepepedirectory.com/wp-content/uploads/2016/09/timetravelpepe.jpg")

@sopel.module.commands('trivia')
def trivia(bot, trigger):
    h = HTMLParser()
    try:
        triviaurl = 'https://opentdb.com/api.php?amount=1&type=multiple'
        r = requests.get(triviaurl)
        j = r.json()
        category = j['results'][0]['category']
        difficulty = j['results'][0]['difficulty']
        question = h.unescape(j['results'][0]['question'])
        answers = [j['results'][0]['correct_answer']]
        for i in j['results'][0]['incorrect_answers']:
                answers.append(i)
        random.shuffle(answers)
        correct_answer = j['results'][0]['correct_answer']
        incorrect_answers = j['results'][0]['incorrect_answers']
        bot.say("This question is in the field of {} and is of {} difficulty: {}".format(category, difficulty, question))
        bot.say("The possible answers are: {}, {}, {}, or {}".format(answers[0], answers[1], answers[2], answers[3]))
        replystr = "If you said {} you are correct, but if you said {}, {}, or {} you should call your parents and complain.".format(correct_answer, incorrect_answers[0], incorrect_answers[1], incorrect_answers[2])
        def f():
            bot.say(replystr)
        t = Timer(10.0, f)
        t.start()
    except:
        bot.say("No trivia for you!")


@sopel.module.commands('tinytrump')
def tinytrump(bot, trigger):
    reddit = praw.Reddit(client_id=client.client_id, client_secret=client.client_secret, user_agent='asdfasdfasdfjhwrgth', username=client.username, password=client.password)
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
def trumbleweed(bot, trigger):
    bot.say("https://rootco.de/2016-03-28-why-use-tumbleweed/")

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

@sopel.module.commands('verge', 'xvg', 'wraith')
def verge(bot, trigger):
    bot.say(u"👻🐕 Don't wraith my dark doge bro! 👻🐕")

vitalikoptions = [
"https://pbs.twimg.com/media/CrWjczJXgAExF2S.jpg",
"mETH, not even once: https://cdn-az.allevents.in/banners/e7df519e0808bac49fa3aaf503aff87d",
"Betteridge's law of headlines: https://fortunedotcom.files.wordpress.com/2016/09/blo_startups_2520x1667.png",
"Casper can survive 51% attacks happening once in a while; we can just delete the attackers' deposits and keep going."
]
@sopel.module.commands('vitalik', 'buterin')
def vitalik(bot, trigger):
    bot.say(random.choice(vitalikoptions))

@sopel.module.commands('wat')
def wat(bot, trigger):
    bot.say("https://www.destroyallsoftware.com/talks/wat")

@sopel.module.commands('wow')
def wow(bot, trigger):
    bot.say("Let he who is without win cast the first 💎: http://wownero.org")

@sopel.module.commands('yoda')
def yoda(bot, trigger):
    bot.say("The optimism is strong in this one")

@sopel.module.commands('xrp')
def xrp(bot, trigger):
    bot.say("We have the best C++ dev team in the world!")

zcashoptions = [
"Trust us guys, we totally smashed that computer up, with like...magnetic baseball bats.",
"https://youtu.be/A51Bl3jkF0c"
]
@sopel.module.commands('zec', 'zcash')
def zcash(bot, trigger):
    bot.say(random.choice(zcashoptions))

@sopel.module.commands('zooko')
def zcash(bot, trigger):
    bot.say("And by the way, I think we can successfully make Zcash too traceable for criminals like WannaCry, but still completely private & fungible.")

@sopel.module.rule('[Tt]est.*')
def test(bot, trigger):
    bot.say("Test failed")

@sopel.module.rule('monerobux o\/')
def wave(bot, trigger):
    #bot.reply(u'‹^› ‹(•_•)› ‹^›')
    bot.reply('hello')
#@sopel.module.rule('[Tt]rump')
#def politics(bot, trigger):
#    bot.reply("politics is the mind killer")

@sopel.module.rule('.*1Dj34exPs3S9qAV1aiGAAADzbashsSVKVP*.')
def scamdouble(bot, trigger):
    bot.say("{} is a scammer and bitcoin is a scam".format(trigger.nick))

@sopel.module.commands('whaleornot')
def whaleornot(bot, trigger):

    if not trigger.group(2):
        bot.say("Gotta have skin in the game to be a big fish! Add some XMR after the command to see what level the player is at!")
    else:
        try:
            xmr_size = float(trigger.group(2))
            if xmr_size <= 0:
                fish_string = "amoeba"
            elif xmr_size < 0.1:
                fish_string = "plankton"
            elif xmr_size >= 0.1 and xmr_size < 0.2:
                fish_string = "Paedocypris"
            elif xmr_size >= 0.2 and xmr_size < 0.5:
                fish_string = "Dwarf Goby"
            elif xmr_size >= 0.5 and xmr_size < 1:
                fish_string = "European Pilchard"
            elif xmr_size >= 1 and xmr_size < 2:
                fish_string = "Goldfish"
            elif xmr_size >= 2 and xmr_size < 5:
                fish_string = "Herring"
            elif xmr_size >= 5 and xmr_size < 10:
                fish_string = "Atlantic Macerel"
            elif xmr_size >= 10 and xmr_size < 20:
                fish_string = "Gilt-head Bream"
            elif xmr_size >= 20 and xmr_size < 50:
                fish_string = "Salmonidae"
            elif xmr_size >= 50 and xmr_size < 100:
                fish_string = "Gadidae"
            elif xmr_size >= 100 and xmr_size < 200:
                fish_string = "Norwegian Delicious Salmon"
            elif xmr_size >= 200 and xmr_size < 500:
                fish_string = "Electric eel"
            elif xmr_size >= 500 and xmr_size < 1000:
                fish_string = "Tuna"
            elif xmr_size >= 1000 and xmr_size < 2000:
                fish_string = "Wels catfish"
            elif xmr_size >= 2000 and xmr_size < 5000:
                fish_string = "Black marlin"
            elif xmr_size >= 5000 and xmr_size < 10000:
                fish_string = "Shark"
            elif xmr_size >= 10000 and xmr_size < 20000:
                fish_string = "Dolphin"
            elif xmr_size >= 20000 and xmr_size < 40000:
                fish_string = "Narwhal"
            elif xmr_size >= 40000 and xmr_size < 60000:
                fish_string = "Orca"
            elif xmr_size >= 60000 and xmr_size < 100000:
                fish_string = "Blue Whale"
            elif xmr_size >= 100000 and xmr_size < 200000:
                fish_string = "Leviathan"
            elif xmr_size >= 200000:
                fish_string = "Cthulu"
            bot.say("{0} level.".format(fish_string))
        except:
            bot.say("Try a base ten representation of a number")

@sopel.module.commands('trebuchet')
def trebuchet(bot, trigger):
    bot.say("Can YOU use a counterweight to launch a 90 kg projectile over 300 meters? Yeah, I thought not.")

@sopel.module.commands('baka')
def baka(bot, trigger):
    bot.say('https://www.youtube.com/watch?v=n5n7CSGPzqw')

@sopel.module.commands('btcdwed')
def btcdwed(bot, trigger):
    bot.say('https://www.youtube.com/watch?v=JZYZoQQ6LJQ')

@sopel.module.commands('wayshegoes')
def wayshegoes(bot, trigger):
    bot.say('https://www.youtube.com/watch?v=3SpihGKmYgY')

@sopel.module.commands('weather')
def weather(bot, trigger):
    wk = client.weather_key
    try:
        if not trigger.group(2):
            location = q="san%20francisco"
        elif trigger.group(2) == 'nioc':
            location = 'new york city'
        else:
            location = trigger.group(2)
        if location.isdigit():
            location = "zip="+location
        else:
            location = "q="+location.replace(' ', '%20')

        r = requests.get('https://api.openweathermap.org/data/2.5/weather?{}&appid={}'.format(location, wk))
        j = r.json()

        location = j['name']+', '+j['sys']['country']
        humidity = j['main']['humidity']
        wind_speed_m_s = j['wind']['speed']
        wind_deg = j['wind']['deg']
        description = j['weather'][0]['description']
        temp_in_c = float(j['main']['temp'])-273
        low_in_c = float(j['main']['temp_min'])-273
        high_in_c = float(j['main']['temp_max'])-273
        temp = temp_in_c
        low = low_in_c
        high = high_in_c

        def calculate_bearing(d):
            dirs = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
            ix = int(round(d / (360. / len(dirs))))
            return dirs[(ix) % len(dirs)]

        direction = calculate_bearing(wind_deg)

        try:
            bot.say("In {} it is {:.1f} C with a low of {:.1f} and high of {:.1f} C, humidity is {}%, winds of {} m/s from the {} with {}.".format(location, temp, low, high, humidity, wind_speed_m_s, direction, description))
        except:
            bot.say("In {} it is {:.2f} C with a low of {:.2f} and high of {:.2f} C, humidity is {}%, winds of {} m/s with {}.".format(location, temp, low, high, humidity, wind_speed_m_s, description))

    except:
        bot.say("The earth is on fire 🌎🔥")
	
@sopel.module.commands('weatherf')
def weatherf(bot, trigger):
    wk = client.weather_key
    try:
        if not trigger.group(2):
            location = q="san%20francisco"
        elif trigger.group(2) == 'nioc':
            location = 'new york city'
        else:
            location = trigger.group(2)
        if location.isdigit():
            location = "zip="+location
        else:
            location = "q="+location.replace(' ', '%20')

        r = requests.get('https://api.openweathermap.org/data/2.5/weather?{}&appid={}'.format(location, wk))
        j = r.json()

        location = j['name']+', '+j['sys']['country']
        humidity = j['main']['humidity']
        wind_speed_m_s = j['wind']['speed']
        wind_deg = j['wind']['deg']
        description = j['weather'][0]['description']
        temp_in_c = float(j['main']['temp'])-273
        low_in_c = float(j['main']['temp_min'])-273
        high_in_c = float(j['main']['temp_max'])-273
        temp = (temp_in_c * 9 / 5 ) + 32
        low = (low_in_c * 9 / 5 ) + 32
        high = (high_in_c * 9 / 5 ) + 32
        wind_speed_mph = float(wind_speed_m_s) * 2.236936

        def calculate_bearing(d):
            dirs = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
            ix = int(round(d / (360. / len(dirs))))
            return dirs[(ix) % len(dirs)]

        direction = calculate_bearing(wind_deg)

        try:
            bot.say("In {} it is {:.1f} F with a low of {:.1f} and high of {:.1f} F, humidity is {}%, winds of {:.1f} mph from the {} with {}.".format(location, temp, low, high, humidity, wind_speed_mph, direction, description))
        except:
            bot.say("In {} it is {:.1f} F with a low of {:.1f} and high of {:.1f} F, humidity is {}%, winds of {:.1f} mph with {}.".format(location, temp, low, high, humidity, wind_speed_mph, description))

    except:
        bot.say("The earth is on fire 🌎🔥")
	
@sopel.module.commands('yeezy', 'kanye', 'ye')
def yeezy(bot, trigger):
    #headers = {'User-Agent': 'monerobux-irc-bot-#wownero'}
    r = requests.get('https://api.kanye.rest')
    #resp.raise_for_status()
    j = r.json()
    #if 'quote' not in blob or not isinstance(blob['quote'], str):
    #    raise Exception('malformed response')
    bot.say(j['quote'])

@sopel.module.commands('mental')
def mental(bot, trigger):
    bot.say('Ahhhhhhhh!!!!')

@sopel.module.commands('biden')
def biden(bot, trigger):
    bot.say('Come on man...')

@sopel.module.commands('smile')
def smile(bot, trigger):
    bot.say('https://archive.is/uqHxO')
