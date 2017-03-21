# -*- coding: utf-8 -*-
import sopel.module
import random
import re
import requests
import praw

@sopel.module.commands('aminorex')
def aminorex(bot, trigger):
    bot.say('if i could replace my wife with a robot...  i might seriously think about it')

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
def banana(bot, trigger):
    bot.say(u'ʕ ·(エ)· ʔ'.encode('utf8'))

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
def dash(bot, trigger):
    bot.say('45SkxgDmcLmW5ByS7w9AG78JuJRvCoVKCdGJWnd4US95CBUAtvdGAdM2oHgZgTGjkEAUcwdqcryM819aqdeiKxHSQC8HkmS', trigger.nick)

@sopel.module.commands('eth')
def eth(bot, trigger):
    bot.say(u'The world computer 💻🌐'.encode('utf8'))

@sopel.module.commands('flip')
def flip(bot, trigger):
    bot.say(u'(╯°□°）╯︵ ┻━┻'.encode('utf8'))

fuckyouoptions = [
"http://imgur.com/Kt8os8v",
"https://pbs.twimg.com/profile_images/502111486915788801/DtB5ruDz_400x400.jpeg",
"http://s2.quickmeme.com/img/70/7073ff0ce9c54f6672f157ebef668c1b6bb123d15fc2e2bc062ec1558f964820.jpg",
"http://static.deathandtaxesmag.com/uploads/2015/01/staff-troll-fuck-you.png",
]
@sopel.module.commands('fuckyou')
def fuckyou(bot, trigger):
    bot.say(random.choice(fuckyouoptions))

@sopel.module.commands('gui')
def gui(bot, trigger):
    bot.say('http://imgur.com/a/hnxfS')

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
def jaxx(bot, trigger):
    bot.say(u'The first, second, third, and fourth amongst joshes.')

@sopel.module.commands('lenny')
def lenny(bot, trigger):
    bot.say(u'( ͡° ͜ʖ ͡°)'.encode('utf8'))

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

@sopel.module.commands('pero')
def pero(bot, trigger):
    bot.say('https://www.youtube.com/watch?v=QqreRufrkxM')

@sopel.module.commands('pleaseconfirm', 'confirm')
def confirm(bot, trigger):
    draw = random.random()
    if draw < 0.20:
        silly_string = "I can confirm that it is true"  
    elif 0.4 > draw >= 0.20:
        silly_string = "This is true"  
    elif 0.6 > draw >= 0.4:
        silly_string = "Fake news"  
    elif 0.8 > draw >= 0.6:
        silly_string = "Alternative fact"  
    elif 1 > draw >= 0.8:
        silly_string = "The outlook is murky, ask again later"  
    bot.say(silly_string)

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

reddit=praw.Reddit(user_agent='monerobux')
@sopel.module.commands('tinytrump')
def tinytrump(bot, trigger):
    try:
        sub=reddit.get_subreddit('tinytrump')
        posts=sub.get_new(limit=100)
        n=random.randint(0,100)
        for i, post in enumerate(posts):
            if i==n:
                bot.say(post.url)
    except:
        bot.say("Something something reddit's servers")

@sopel.module.commands('trump')
def trump(bot, trigger):
    bot.say("Monero is the best crypto, believe me, I know crypto and it's going to be yuuuuuuuge!")

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
"ur mom is Amanda B Johnson"
]  
@sopel.module.commands('urmom', 'yourmom', 'yomom', 'yomomma')
def urmom(bot, trigger):
    bot.say(random.choice(urmomoptions))

@sopel.module.commands('wat')
def wat(bot, trigger):
    bot.say("https://www.destroyallsoftware.com/talks/wat")

@sopel.module.commands('zec', 'zcash')
def zcash(bot, trigger):
    bot.say('Trust us guys, we totally smashed that computer up, with like...magnetic baseball bats.')

@sopel.module.rule('monerobux o\/')
def wave(bot, trigger):
    #bot.reply(u'‹^› ‹(•_•)› ‹^›'.encode('utf8'))
    bot.reply('hello')
#@sopel.module.rule('[Tt]rump')
#def politics(bot, trigger):
#    bot.reply("politics is the mind killer")
