# Copyright (C) 2013 - Russell Bryant
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import urllib
import re
import sys
from sopel import module


def get_quote(symbol):
    url = 'http://finance.google.com/finance?q=%s' % symbol
    content = urllib.urlopen(url).read()
    m = re.search('id="ref_(.*?)">(.*?)<', content)
    if m:
        quote = m.group(2)
    else:
        quote = 'no quote available for: "%s"' % symbol
        return quote

    m = re.search('class="chg" id="ref_\d+_c">(.*?)<', content)
    if m:
        quote += ' | %s' % m.group(1)

    m = re.search('class="chg" id="ref_\d+_cp">(.*?)<', content)
    if m:
        quote += ' | %s' % m.group(1)

    return quote


def quote(bot, input):
    symbol = input.group(2)
    bot.say(get_quote(symbol))
quote.commands = ['quote']
