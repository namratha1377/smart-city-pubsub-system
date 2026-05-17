import paho.mqtt.client as mqtt

broker = "localhost"
topic = "pollution/alerts"

def on_message(client, userdata, message):

    print("\n========== HEALTH ALERT ==========")
    print(message.payload.decode())
    print("==================================")

client = mqtt.Client()

client.connect(broker, 1883)

client.subscribe(topic)

client.on_message = on_message

print("Health Department Listening...")

client.loop_forever()