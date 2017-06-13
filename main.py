from rtmbot import RtmBot
import os

config = {
	'DAEMON' : False,
	'DEBUG' :  True,
	'SLACK_TOKEN' : os.environ['SLACK_TOKEN'],
	'ACTIVE_PLUGINS' : ['plugins.presence.PresenceListener']
}
bot = RtmBot(config)

while True:
	bot.start()
	# Occassionally we got https://api.slack.com/events/team_migration_started this event, that closes websocket
	time.sleep(5)