#!/bin/bash

USAGE="Usage: start_selenium <nodeConfig> <SELENIUM_HUB_HOST> <SELENIUM_HUB_PORT>"

NODE_CONFIG="$1"
SELENIUM_HUB_HOST="$2"
SELENIUM_HUB_PORT="$3"
SELENIUM_NODE_PORT="$4"

if [ "$NODE_CONFIG" = "" ]; then
  echo "ERROR: Missing NODE_CONFIG." $USAGE
  exit -1;
fi

if [ "$SELENIUM_HUB_HOST" = "" ]; then
  echo "ERROR: Missing SELENIUM_HUB_HOST." $USAGE
  exit -1;
fi

if [ "$SELENIUM_HUB_PORT" = "" ]; then
  echo "ERROR: Missing SELENIUM_HUB_PORT." $USAGE
  exit -1;
fi

if [ "$SELENIUM_NODE_PORT" = "" ]; then
  echo "ERROR: Missing SELENIUM_NODE_PORT." $USAGE
  exit -1;
fi

export DISPLAY=:99

/etc/init.d/xvfb start
java -jar /var/lib/selenium/selenium-server-standalone-2.42.2.jar \
-role node \
-p $SELENIUM_NODE_PORT \
-nodeConfig $NODE_CONFIG \
-hub http://$SELENIUM_HUB_HOST:$SELENIUM_HUB_PORT/grid/register
