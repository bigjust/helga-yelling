import random
import re

from helga.db import db
from helga.plugins import preprocessor

def is_shout(message):
    """
    Returns `True` if message is determined to be a loud rambling of a
    madperson.

    We should verify letters and there should be atleast 3
    """

    regex = re.compile(r'[^a-zA-Z]')

    stripped = regex.sub('', message)

    if len(stripped) > 1 and stripped.upper() == regex.sub('', message):
        return True

    return False

@preprocessor
def yelling(client, channel, nick, message):

    if is_shout(message):

        count = db.yelling.find({
            'channel': channel,
        }).count()

        if count:
            random_resp = db.yelling.find({
                'channel': channel
            })[random.randrange(count)]
            client.msg(channel, random_resp['msg'])

        db.yelling.insert({
            'msg': message,
            'channel': channel,
        })

    return (channel, nick, message)
