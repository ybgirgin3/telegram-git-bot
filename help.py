#!/usr/bin/python3
#Filename: help.py
from telegram.ext import Updater


def help(bot, update):
	help = update.message.reply_text("""
		Basically usage of this bot

		/help: shows this message
		/commands : shows the specs that can get from your company's / community's github and it's inner commands
		--> git's inner commands
	 		/name: 
	 			shows name of your company/community
	 		/email: 
	 			shows email address that defined in github page
	 		/web_page: 
	 			shows official website of company/community
	 		/web_page_controller: 
	 			shows host url that you using for making changes in your website
	 		/git_p_repos: 
	 			shows how much repo is currently released in github page
	 		/git_p_gists: 
	 			shows how much gists is currently released in github page
	 		/git_follow: 
	 			shows how many people following you and how many people you are following
	 		/git_url: 
	 			shows your direct url of your github page's 
	 		/git_members: 
	 			shows managers members name and their official github accounts url (not working properly)
	 		/founded: 
	 			shows the date of the company/community established (just for honor)
			/dog:
				shows some kind of cute dog pics (just for fun)
		""")
	return help

# End of help.py
