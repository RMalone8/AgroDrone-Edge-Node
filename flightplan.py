import json
from dotenv import load_dotenv
import os
import requests
import time

load_dotenv()

BACKEND_URL = 'http://localhost:8787'
DEVICE_TOKEN = os.getenv("DEVICE_TOKEN")

while True:
    # check for any new flightplans
    response = requests.get(BACKEND_URL + "/flightplan",
                headers={"Authorization": "Bearer " + DEVICE_TOKEN})
    

    # TODO
    # add Siara's script to process the waypoints

    # write to file to be offloaded to drone
    with open("data.json", "w") as f:
        json.dump(response.json(), f, indent=4)

    time.sleep(60) # wait for a minute