import json
from dotenv import load_dotenv
import os
import paho.mqtt.client as mqtt
import waypoints

load_dotenv()

MQTT_HOST = os.getenv("MQTT_HOST", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
WAYPOINT_PATH = os.getenv("WAYPOINT_PATH")

def on_connect(client, _userdata, _flags, rc):
    if rc == 0:
        print("Connected to MQTT broker, subscribing to flightplan topic...")
        client.subscribe("flightplan")
    else:
        print(f"Failed to connect to MQTT broker, return code: {rc}")

def on_message(_client, _userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        print("Received flight plan, checking if it's new...")

        if os.path.exists(WAYPOINT_PATH):
            with open(WAYPOINT_PATH, "r") as f:
                past_waypoints = json.load(f)
            if past_waypoints["missionId"] == data["missionId"]:
                print("Flight plan already processed, skipping.")
                return

        print("Processing new flight plan of missionId:", data["missionId"])
        wp = waypoints.create_waypoints(data)
        with open(WAYPOINT_PATH, "w") as f:
            json.dump(wp, f, indent=4)

    except Exception as e:
        print("Error processing flight plan message:", e)

def main():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(MQTT_HOST, MQTT_PORT)
    print(f"Listening for flight plans on {MQTT_HOST}:{MQTT_PORT}...")
    client.loop_forever()

if __name__ == "__main__":
    main()
