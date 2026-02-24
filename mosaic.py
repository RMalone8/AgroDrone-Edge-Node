import json
from dotenv import load_dotenv
import os
import requests

load_dotenv()

BACKEND_URL = 'http://localhost:8787'
DEVICE_TOKEN = os.getenv("DEVICE_TOKEN")

def main():
    # TODO
    # process the images

    # send the final mosaic to the cloud
    with open("test_image.jpg", "rb") as f:
        files = {"mosaic": ( "test_image.jpg", f, "image/jpeg" )}
        response = requests.post(BACKEND_URL + "/mosaic",
                    headers={"Authorization": "Bearer " + DEVICE_TOKEN},
                    files=files)
        
    print(response.status_code, response.text)

if __name__ == '__main__':
    main()