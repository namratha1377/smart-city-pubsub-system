import paho.mqtt.client as mqtt
import time
import random
import json

broker = "localhost"
topic = "traffic/alerts"

client = mqtt.Client()
client.connect(broker, 1883)

traffic_events = [
    "Heavy traffic near Silk Board",
    "Accident at MG Road",
    "Signal failure at Whitefield",
    "Traffic congestion at KR Puram",
    "Road blockage near Electronic City"
]

while True:

    event = {

        "department": "Traffic Department",
        "type": "Traffic",
        "message": random.choice(traffic_events),
        "severity": random.choice([
            "LOW",
            "MEDIUM",
            "HIGH"
        ]),
        "timestamp": time.strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    }

    client.publish(
        topic,
        json.dumps(event)
    )

    print("\nTRAFFIC EVENT SENT")
    print(event)

    time.sleep(5)