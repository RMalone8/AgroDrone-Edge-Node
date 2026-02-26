import json
from dotenv import load_dotenv
import os
import requests

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL")
DEVICE_TOKEN = os.getenv("DEVICE_TOKEN")
DATA_DIRECTORY = os.getenv("DATA_DIRECTORY")

def main():
    # TODO
    # process the images

    # send the final mosaic to the cloud
    with open("../test_image.jpg", "rb") as f:
        files = {"mosaic": ( "test_image.jpg", f, "image/jpeg" )}
        response = requests.post(BACKEND_URL + "/mosaic",
                    headers={"Authorization": "Bearer " + DEVICE_TOKEN},
                    files=files)
        
    # cleanup: remove flag directory
    if os.path.exists(DATA_DIRECTORY + "/SUCCESS.txt"):
        os.remove(DATA_DIRECTORY + "/SUCCESS.txt")
        
    print(response.status_code, response.text)

if __name__ == '__main__':
    main()