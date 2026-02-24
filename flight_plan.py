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
    response = requests.get(BACKEND_URL + "/flightplan/latest",
                headers={"Authorization": "Bearer " + DEVICE_TOKEN})

    data = response.json()

    with open("waypoints.json", "r") as f:
        past_waypoints = json.load(f)

    # checking if this mission already exists. If not, create waypoints for it
    if past_waypoints["missionId"] != data["missionId"]:
    
        wp = waypoints.create_waypoints(response.json())

        print("Waypoints created!")

        # write to file to be offloaded to drone
        with open("waypoints.json", "w") as f:
            json.dump(wp, f, indent=4)

        # TODO
        # need to set some flag so that this new mission can be sent to the drone
        
    else:
        print("Mission Already Exists")

    print("Sleeping...")
    time.sleep(15) # wait for a minute