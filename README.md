# Telegram Git Bot

Basic telegram bot for getting any community informations from telegram without entering browser and github account

**How to make it work**

Before running this python telegram bot you have to install required telegram bot for python;
       
```sh
pip3 install python-telegram-bot
```
then follow telegram bot creation tutorial from https://core.telegram.org/bots because you will need bot key to make this bot work. You will get the key from telegram's BotFather after giving your bot name and other needed specificaton. Key is important because everybody that who has this key has access to change your bot completely. You need to add key to here:

```py
# telegram-github-bot.py line: 20
updater = Updater("your telegram bot key")	# ADD YOUR KEY HERE
```

**Github Entegration**

Github entegration is bit of complex (at least for me).
You need to get your personal account's or community account's api from https://developer.github.com/v3/


For example;

Api needs to be like "https://api.github.com/orgs/(your_community/organization_name)" for organization/community account

You can run your api in the browser to control if it's running truely or not.

***API NEEDS TO BE A JSON FILE***

After getting api you need to paste the api url to;

```py
# git_process.py line: 14
def jsonProcess():
	f = requests.get("your community github api").text 	# ADD YOUR API HERE
	global data
    	data = json.loads(f)
    	return data
```
and it's done !!.

Now you can test your telegram bot with running 'telegram-github-bot.py' file. 
For getting informations you have to give your bot **/commands** command and also you can give your bot **/dog** command to see silly, cute, awesome dog pics :)

***This file wrote in python3 and it's highly recommended for avoid errors***
