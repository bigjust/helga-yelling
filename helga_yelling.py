import random
import re

from helga import log
from helga.db import db
from helga.plugins import preprocessor, command

logger = log.getLogger(__name__)

def is_shout(message):
    """
    Returns `True` if message is determined to be a loud rambling of a
    madperson.

    We should verify letters and there should be atleast 2
    """

    regex = re.compile(r'[^a-zA-Z]')
    stripped = regex.sub('', message)

    if len(stripped) > 1 and stripped.upper() == regex.sub('', message):
        return True

    return False


@preprocessor
@command('yell', help='Usage: yell remove <pattern>')
def yelling(client, channel, nick, message, *args):

    if len(args) == 0:
        # Preprocessor

        if is_shout(message):

            count = db.yelling.find({
                'channel': channel,
            }).count()

            if count:
                random_resp = db.yelling.find({
                    'channel': channel
                })[random.randrange(count)]

                client.msg(channel, random_resp['msg'])

            db.yelling.update_one({
                'msg': message,
                'channel': channel,
            }, { '$set': { 'msg': message } }, upsert=True)

        return (channel, nick, message)

    if len(args) == 2:
        logger.debug('args: {}'.format(args))

        cmd, yell = args[1][0], args[1][1:]

        if cmd != 'remove':
            return

        yell_to_forget = ' '.join(yell)

        logger.debug('will attempt to purge: {}'.format(yell_to_forget))

        remove_result = db.yelling.delete_one({
            'msg': yell_to_forget,
            'channel': channel,
        })

        logger.debug('remove_result: {}'.format(remove_result.deleted_count))

        if remove_result.deleted_count == 1:
            return 'done.'
        else:
            return 'not found :('
