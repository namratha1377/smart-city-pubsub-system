from flask import Flask, render_template
import sqlite3
import threading
import paho.mqtt.client as mqtt
import json

app = Flask(__name__)

DB_NAME = "events.db"

# DATABASE SETUP

def init_db():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS events (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            department TEXT,

            type TEXT,

            message TEXT,

            severity TEXT,

            timestamp TEXT

        )

    """)

    conn.commit()
    conn.close()

init_db()

# HOME PAGE

@app.route('/')

def index():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # TRAFFIC EVENTS

    cursor.execute("""

        SELECT * FROM events

        WHERE type='Traffic'

        ORDER BY id DESC

        LIMIT 10

    """)

    traffic_events = cursor.fetchall()

    # POLLUTION EVENTS

    cursor.execute("""

        SELECT * FROM events

        WHERE type='Pollution'

        ORDER BY id DESC

        LIMIT 10

    """)

    pollution_events = cursor.fetchall()

    # WEATHER EVENTS

    cursor.execute("""

        SELECT * FROM events

        WHERE type='Weather'

        ORDER BY id DESC

        LIMIT 10

    """)

    weather_events = cursor.fetchall()

    # COUNTS

    cursor.execute("""

        SELECT COUNT(*)

        FROM events

        WHERE type='Traffic'

    """)

    traffic_count = cursor.fetchone()[0]

    cursor.execute("""

        SELECT COUNT(*)

        FROM events

        WHERE type='Pollution'

    """)

    pollution_count = cursor.fetchone()[0]

    cursor.execute("""

        SELECT COUNT(*)

        FROM events

        WHERE type='Weather'

    """)

    weather_count = cursor.fetchone()[0]

    conn.close()

    return render_template(

        "index.html",

        traffic_events=traffic_events,

        pollution_events=pollution_events,

        weather_events=weather_events,

        traffic_count=traffic_count,

        pollution_count=pollution_count,

        weather_count=weather_count

    )

# MQTT MESSAGE RECEIVER

def on_message(client, userdata, msg):

    data = json.loads(msg.payload.decode())

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""

        INSERT INTO events
        (department, type, message, severity, timestamp)

        VALUES (?, ?, ?, ?, ?)

    """, (

        data["department"],
        data["type"],
        data["message"],
        data["severity"],
        data["timestamp"]

    ))

    conn.commit()
    conn.close()

    print("\nSAVED TO DATABASE")
    print(data)

# MQTT THREAD

def mqtt_thread():

    client = mqtt.Client()

    client.connect("localhost", 1883)

    client.subscribe("traffic/alerts")
    client.subscribe("pollution/alerts")
    client.subscribe("weather/alerts")

    client.on_message = on_message

    client.loop_forever()

threading.Thread(target=mqtt_thread).start()

# RUN FLASK

if __name__ == '__main__':

    app.run(debug=True)