import json
from dotenv import load_dotenv
import os
import paho.mqtt.client as mqtt

load_dotenv()

MQTT_HOST = os.getenv("MQTT_HOST", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
TELEMETRY_PATH = os.getenv("TELEMETRY_PATH")
TOPIC = "telemetry"

def main():
    # read the telemetry file
    try:
        with open(TELEMETRY_PATH, "r") as f:
            telemetry = json.load(f)
    except Exception as e:
        print(f"Error Opening Telemetry File at {TELEMETRY_PATH}: ", e)
        return

    # publish telemetry to MQTT broker
    try:
        client = mqtt.Client()
        client.connect(MQTT_HOST, MQTT_PORT)
        result = client.publish(TOPIC, json.dumps(telemetry))
        result.wait_for_publish()
        client.disconnect()
        print(f"Telemetry published to {MQTT_HOST}:{MQTT_PORT} on topic '{TOPIC}'")
    except Exception as e:
        print("Error Publishing Telemetry to MQTT: ", e)

if __name__ == '__main__':
    main()
