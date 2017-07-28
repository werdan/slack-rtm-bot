from rtmbot import RtmBot
import os
import traceback
import sys
import time

config = {
	'DAEMON' : False,
	'DEBUG' :  True,
	'SLACK_TOKEN' : os.environ['SLACK_TOKEN'],
	'ACTIVE_PLUGINS' : ['plugins.presence.PresenceListener']
}
bot = RtmBot(config)

while True:
	try:
		bot.start()
	# Occassionally we got https://api.slack.com/events/team_migration_started this event, that closes websocket
	except:
		exc_type, exc_value, exc_traceback = sys.exc_info()
		lines = traceback.format_exception(exc_type, exc_value, exc_traceback)
		print ''.join('!! ' + line for line in lines)
	time.sleep(5)