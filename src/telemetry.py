import json
from dotenv import load_dotenv
import os
import requests

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL")
DEVICE_TOKEN = os.getenv("DEVICE_TOKEN")
TELEMETRY_PATH = os.getenv("TELEMETRY_PATH")

def main():
    # read the telemetry file
    try:
        with open(TELEMETRY_PATH, "r") as f:
            telemetry = json.load(f)
    except Exception as e:
        print(f"Error Opening Telemetry File at {TELEMETRY_PATH}: ", e)

    # send telemetry
    try:
        response = requests.post(BACKEND_URL + "/telemetry",
                    headers={"Authorization": "Bearer " + DEVICE_TOKEN},
                    json=telemetry)
    except Exception as e:
        print("Error Sending Telemetry to Backend: ", e)

    print(response, response.status_code)

if __name__ == '__main__':
    main()