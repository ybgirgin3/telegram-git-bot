#!/usr/bin/python3
from help import *
from hello import *
from git_process import *
from telegram.ext import Updater, CommandHandler
# fun shit
from dog_process import *


# main functions that makes other functions work
def main():
    updater = Updater('651372077:AAFCyxgIH2FX9s0WMtnbx1TtZtUV33ZqF48')
    dp = updater.dispatcher

    # handlers
    dp.add_handler(CommandHandler("hello", hello))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("dog", dog))
    dp.add_handler(CommandHandler("commands", commands))
    dp.add_handler(CommandHandler("name", name))
    dp.add_handler(CommandHandler("email", email))
    dp.add_handler(CommandHandler("web_page", web_page))
    dp.add_handler(CommandHandler("web_page_controller", web_page_controller))
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
