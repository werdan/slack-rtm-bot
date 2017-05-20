### Plugin handles status changes which can be used to remind user about actions to be done once online [active]
### Example implementation logs to BigQuery

from __future__ import print_function
from __future__ import unicode_literals
from rtmbot.core import Plugin
from google.cloud import bigquery
import time
import os

class PresenceListener(Plugin):

    module = 'PresenceListener'

    # Table is expected to have 3 fields: timestamp (TIMESTAMP), member_id (STRING), status (STRING)

    def __init__(self, slack_client,plugin_config):
        super(self.__class__, self).__init__()
        self.table = bigquery.Client().dataset('slack').table('presence')
        self.table.reload()

    def process_presence_change(self, data):
        rows = [(time.strftime('%Y-%m-%d %H:%M:%S'),data['user'],data['presence'])]
        print ("Handling presence_change")
        print (rows[0])
        errors = self.table.insert_data(rows)
        if errors:
            print ("Errors found")
            print (errors)

