#!/usr/bin/python3
# Filename: hello.py
from telegram.ext import Updater

# makes you feel welcome
def hello(bot, update):
    name = update.message.from_user.first_name
    hello = update.message.reply_text("""
    	Hello Welcome {}
    	/help for basic usage tutorial,
    	/commands for directly diving into bot
    	""".format(name))
    return hello

# End of hello.py
