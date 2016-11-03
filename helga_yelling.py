import random

from helga.db import db

from helga.plugins import preprocessor

@preprocessor
def yelling(client, channel, nick, message):

    if message.upper() == message:

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
