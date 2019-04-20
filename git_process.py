#!/usr/bin/python3
# Filename: git_process.py
from telegram.ext import Updater
############## git information downloader #########
import json
import requests 

def jsonProcess():
    f = requests.get("your api here").text
    global data
    data = json.loads(f)
    return data

############


# git process
def commands(bot, update):
    # p_repos   : public repos
    # p_gists   : public gists
    # follow    : followers & following
    # url       : github account
    # founded   : founded date of community
    defining = update.message.reply_text("""commands that you can use:
                    /name,
                    /email,
                    /web_page,
                    /web_page_controller,
                    /git_p_repos,
                    /git_p_gists,
                    /git_follow,
                    /git_url,
                    /git_members
                    /founded,
                """)
    return defining

# other options

# displays git name
def name(bot, update):
    jsonProcess()
    git_name = update.message.reply_text(data['name'])
    return git_name


# displays git email address
def email(bot, update):
    jsonProcess()
    git_email = update.message.reply_text(data['email'])
    return git_email


# displays how much public git repos existed
def git_p_repos_count(bot, update):
    jsonProcess()
    git_p_repos_count = update.message.reply_text(data['public_repos'])
    return git_p_repos_count


# displays repos (!)
def git_repos(bot, update):
    jsonProcess()
    git_p_repos = update.message.reply_text(data['repos_url'])
    return git_p_repos


# displays how much public gist existed
def git_p_gists_count(bot, update):
    jsonProcess()
    git_p_gists_count = update.message.reply_text(data['public_repos'])
    return git_p_gists_count


# displays how much followers community has
def git_follow(bot, update):
    jsonProcess()
    git_followers = update.message.reply_text(data['followers'])
    git_following = update.message.reply_text(data['following'])
    twins = git_followers, git_following
    return twins


# displays offical github repository url of community
def git_url(bot, update):
    jsonProcess()
    git_url = update.message.reply_text(data['html_url'])
    return git_url


# the day community founded
def founded(bot, update):
    jsonProcess()
    founded = update.message.reply_text(data['created_at'])
    return founded


# displays member's name
def git_members(bot, update):
    jsonProcess()
    members = update.message.reply_text(data['members_url'])
    return members

def web_page(bot, update):
    jsonProcess()
    web_page = update.message.reply_text(data['blog'])
    return web_page


# End of git_process.py

