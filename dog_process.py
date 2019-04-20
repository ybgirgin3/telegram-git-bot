#!/usr/bin/python3
# Filename: dog_process.py
"""
Author: Yusuf Berkay Girgin
date: 6 April 2019
"""
import json
import requests
from telegram.ext import Updater

# api getter
def get_url():
    # we use random.dog for example but you can change json file with your fav site
    contents = requests.get("https://random.dog/woof.json").json()
    url = contents['url']
    return url

def dog(bot, update):
    get_url()
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

# End of dog_process.py
