#!/bin/bash

DRONE_PI_IP="10.10.10.10" # will be configured
DRONE_PI_USER="sr-design"
LOCAL_FILE="/home/sr-design/agrodrone-system/flightplans/waypoints.json"
REMOTE_DEST="/home/sr-design/agrodrone-system/flightplans/"

rsync -az $LOCAL_FILE $DRONE_PI_USER@$DRONE_PI_IP:$REMOTE_DEST