#!/usr/bin/env python


import os
import subprocess
import string
import textwrap
import json

from maestro.guestutils import *
from maestro.extensions.logging.logstash import run_service

NODE_CONFIG = '/var/lib/selenium/nodeConfig.json'

with open(NODE_CONFIG, 'r') as f:
    data = json.load(f)
    f.close()
    
data["configuration"]["host"] = get_container_host_address()
data["configuration"]["port"] = os.environ.get('SELENIUM_NODE_PORT', 5555)
data["configuration"]["hubHost"] = os.environ.get('SELENIUM_HUB_HOST', get_container_host_address())
data["configuration"]["hubPort"] = os.environ.get('SELENIUM_HUB_PORT', 4444)

with open(NODE_CONFIG, 'w+') as f:
    f.write(json.dumps(data))
    f.close()

SUPERVISORD_CONF_FILE = '/etc/supervisor/conf.d/supervisord.conf'

with open(SUPERVISORD_CONF_FILE) as f:
    conf = string.Template(f.read())

with open(SUPERVISORD_CONF_FILE, 'w+') as f:
    f.write(conf.substitute(
      SELENIUM_HUB_HOST=os.environ.get('SELENIUM_HUB_HOST', get_container_host_address()),
      SELENIUM_HUB_PORT=os.environ.get('SELENIUM_HUB_PORT', 4444),
      SELENIUM_NODE_PORT=os.environ.get('SELENIUM_NODE_PORT', 5555)))

# Start Supervisord in the foreground.
os.execl('/usr/bin/supervisord', '-n')
