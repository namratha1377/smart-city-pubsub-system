import paho.mqtt.client as mqtt
import time
import random
import json

broker = "localhost"
topic = "pollution/alerts"

client = mqtt.Client()
client.connect(broker, 1883)

pollution_events = [
    "AQI dangerous near Industrial Area",
    "Smoke detected in City Center",
    "High CO2 levels near factory zone",
    "Dust pollution increasing rapidly",
    "Toxic gas leakage warning"
]

while True:

    event = {

        "department": "Health Department",
        "type": "Pollution",
        "message": random.choice(
            pollution_events
        ),
        "severity": random.choice([
            "MEDIUM",
            "HIGH",
            "CRITICAL"
        ]),
        "timestamp": time.strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    }

    client.publish(
        topic,
        json.dumps(event)
    )

    print("\nPOLLUTION EVENT SENT")
    print(event)

    time.sleep(7)