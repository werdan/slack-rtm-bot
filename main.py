from rtmbot import RtmBot
import os

config = {
	'DAEMON' : False,
	'DEBUG' :  False,
	'SLACK_TOKEN' : os.environ['SLACK_TOKEN'],
	'ACTIVE_PLUGINS' : ['plugins.presence.PresenceListener']
}
bot = RtmBot(config)
bot.start()