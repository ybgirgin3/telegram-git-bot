#!/usr/bin/python3
"""
Author: Yusuf Berkay Girgin
date: 6 April 2019
"""

from git_process import *
from dog_process import *
# from cat_process import *
from telegram.ext import Updater, CommandHandler

# makes you feel welcome
def hello(bot, update):
    name = update.message.from_user.first_name
    update.message.reply_text("Hello Welcome {}".format(name))


# main functions that makes other functions work
def main():
    updater = Updater("your telegram bot key")
    dp = updater.dispatcher

    # handlers
    dp.add_handler(CommandHandler("hello", hello))
    dp.add_handler(CommandHandler("dog", dog))
    # dp.add_handler(CommandHandler("cat", cat))
    dp.add_handler(CommandHandler("commands", commands))
    dp.add_handler(CommandHandler("name", name))
    dp.add_handler(CommandHandler("email", email))
    dp.add_handler(CommandHandler("git_repos", git_repos))
    dp.add_handler(CommandHandler("git_p_repos_count", git_p_repos_count))
    dp.add_handler(CommandHandler("git_p_gists_count", git_p_gists_count))
    dp.add_handler(CommandHandler("git_follow", git_follow))
    dp.add_handler(CommandHandler("git_url", git_url))
    dp.add_handler(CommandHandler("git_members", git_members))
    dp.add_handler(CommandHandler("founded", founded))


    # to make bot running
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
