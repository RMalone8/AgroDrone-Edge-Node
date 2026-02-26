import json
from dotenv import load_dotenv
import os
import requests
import time
import waypoints

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL")
DEVICE_TOKEN = os.getenv("DEVICE_TOKEN")
WAYPOINT_PATH = os.getenv("WAYPOINT_PATH")

def main():
    while True:
        # check for any new flightplans
        response = requests.get(BACKEND_URL + "/flightplan/latest",
                    headers={"Authorization": "Bearer " + DEVICE_TOKEN})

        data = response.json()

        if os.path.exists(WAYPOINT_PATH):
            with open(WAYPOINT_PATH, "r") as f:
                past_waypoints = json.load(f)
            # checking if this mission already exists. If not, create waypoints for it
            if past_waypoints["missionId"] != data["missionId"]:
                waypoint_processing(data) 
        else:
            waypoint_processing(data)

        time.sleep(120) # sleep for two minutes

def waypoint_processing(data: dict):
    # create waypoints
    wp = waypoints.create_waypoints(data)

    # write to file to be offloaded to drone
    with open(WAYPOINT_PATH, "w") as f:
        json.dump(wp, f, indent=4)

if __name__ == "__main__":
    main()