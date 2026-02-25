import json
from dotenv import load_dotenv
import os
import requests
import time

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL")
DEVICE_TOKEN = os.getenv("DEVICE_TOKEN")

while True:
    # read the telemetry file
    with open("../telemetry.json", "r") as f:
        telemetry = json.load(f)

    print(telemetry)

    # send telemetry
    response = requests.post(BACKEND_URL + "/telemetry",
                headers={"Authorization": "Bearer " + DEVICE_TOKEN},
                json=telemetry)

    time.sleep(60) # wait for a minute