# -*- coding: utf-8 -*-
import requests
import sopel.module

@sopel.module.commands('gp2', 'ai')
def gp2(bot, trigger):
    # bot.say("bomb-on ruined it for everyone. thanks bomb-on")
    text = trigger.group(2)
    r = requests.post(
        "https://api.deepai.org/api/text-generator",
        data={
            'text': text,
        },
        headers={'api-key': '4509ed67-e409-4e68-821a-05a15ce6b052'}
    )
    #bot.say(r.json())
    bot.say(r.json()['output'].split('\n\n')[0])
    bot.say(r.json()['output'].split('\n\n')[1])
    bot.say(r.json()['output'].split('\n\n')[2])
    #bot.say("full output at http://ai.wownero.com")
    #stringtowrite = r.json['output'].encode('utf8')
    #with open("/root/www/index.html", "w") as f:
    #    f.write(stringtowrite)
