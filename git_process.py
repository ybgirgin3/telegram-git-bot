#!/usr/bin/python3
"""
Author: Yusuf Berkay Girgin
date: 6 April 2019
"""
# Filename: git_process.py
from telegram.ext import Updater

############## git information fetcher #########
import json
import requests 

def jsonProcess():
    f = requests.get("your community github api").text
    global data
    data = json.loads(f)
    return data

############################

# git process
def commands(bot, update):
    # p_repos   : public repos
    # p_gists   : public gists
    # follow    : followers & following
    # url       : github account
    # founded   : the date of community founded
    defining = update.message.reply_text("""kullanabileceğiniz komutlar:
                    /name,
                    /email,
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


# End of git_process.py

