import json
from dotenv import load_dotenv
import os
import requests
import time
import waypoints

load_dotenv()

BACKEND_URL = 'http://localhost:8787'
DEVICE_TOKEN = os.getenv("DEVICE_TOKEN")

while True:
    # check for any new flightplans
    response = requests.get(BACKEND_URL + "/flightplan",
                headers={"Authorization": "Bearer " + DEVICE_TOKEN})

    # TODO
    # check if the backend indicated that there were any changes to the mission, then process and flag to be sent to the drone

    wp = waypoints.create_waypoints(response.json())

    # write to file to be offloaded to drone
    with open("waypoints.json", "w") as f:
        json.dump(wp, f, indent=4)

    time.sleep(60) # wait for a minute