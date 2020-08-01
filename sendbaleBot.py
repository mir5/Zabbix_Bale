#!/usr/bin/env python
import logging
from time import sleep

import telegram
from telegram.error import NetworkError, Unauthorized

update_id = None


def main():
    global update_id
    bot = telegram.Bot(token='876123331:cbb44078815w2323ewr342ewr234er34543cd4',
                       base_url="https://tapi.bale.ai/")

    try:
        bot.delete_webhook()
        update_id = bot.get_updates()[0].update_id
    except IndexError:
        update_id = None


    while True:
        try:
            echo(bot)
            sleep(2)
        except NetworkError:
            sleep(1)
        except Unauthorized:
            # The user has removed or blocked the bot.
            update_id += 1


def echo(bot):
    global update_id
    # Request updates after the last update_id
    for update in bot.get_updates(offset=update_id, timeout=10):
        update_id = update.update_id + 1

        if update.message:  # your bot can receive updates without messages
            # Reply to the message
            if (update.message.text=="Code"):
               update.message.reply_text("Your Code is: "+ str(update.message.chat.id) )


main()