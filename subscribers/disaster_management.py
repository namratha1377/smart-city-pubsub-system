import paho.mqtt.client as mqtt

broker = "localhost"

topics = [
    ("traffic/alerts", 0),
    ("pollution/alerts", 0),
    ("weather/alerts", 0)
]

def on_message(client, userdata, message):

    print("\n====== DISASTER MANAGEMENT ALERT ======")
    print(message.payload.decode())
    print("=======================================")

client = mqtt.Client()

client.connect(broker, 1883)

client.subscribe(topics)

client.on_message = on_message

print("Disaster Management Listening...")

client.loop_forever()