import paho.mqtt.client as mqtt
import time
import random
import json

broker = "localhost"
topic = "weather/alerts"

client = mqtt.Client()
client.connect(broker, 1883)

weather_events = [
    "Heavy rainfall warning",
    "Cyclone alert in coastal area",
    "Thunderstorm approaching city",
    "Flood risk detected",
    "Extreme heatwave warning"
]

while True:

    event = {

        "department": "Disaster Management",
        "type": "Weather",
        "message": random.choice(
            weather_events
        ),
        "severity": random.choice([
            "LOW",
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

    print("\nWEATHER EVENT SENT")
    print(event)

    time.sleep(10)