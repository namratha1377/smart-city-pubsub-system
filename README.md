# Smart City Distributed Publish-Subscribe Event Notification System

## Project Overview

This project implements a Distributed Publish-Subscribe Event Notification System for a Smart City environment using MQTT protocol.

Different smart city sensors continuously publish events such as:

- Traffic alerts
- Pollution alerts
- Weather alerts

Relevant departments subscribe only to required topics and receive real-time notifications.

The system demonstrates distributed communication using the Publish-Subscribe architectural pattern.

---

# Features

- Distributed MQTT communication
- Multiple publishers and subscribers
- Real-time event notifications
- Department-wise routing
- Dashboard visualization
- Analytics charts
- Severity-based alerts
- SQLite database logging
- Professional UI dashboard

---

# Technologies Used

- Python
- Flask
- MQTT
- Eclipse Mosquitto
- SQLite
- HTML
- CSS
- Chart.js

---

# Project Structure

smart_city_pubsub/

├── dashboard/

├── publishers/

├── subscribers/

├── README.md

---

# Publishers

- Traffic Sensor
- Pollution Sensor
- Weather Sensor

These continuously publish events to MQTT topics.

---

# Subscribers

- Traffic Department
- Health Department
- Disaster Management

Each subscriber receives only relevant alerts.

---

# MQTT Topics

| Topic | Purpose |
|---|---|
| traffic/alerts | Traffic events |
| pollution/alerts | Pollution events |
| weather/alerts | Weather events |

---

# Dashboard Features

- Department-wise alert panels
- Analytics cards
- Charts and visualization
- Severity indicators
- Real-time monitoring

---

# How To Run

## Start MQTT Broker

```bash
mosquitto -v 

Start Publishers 
python publishers/traffic_sensor.py 
python publishers/pollution_sensor.py 
python publishers/weather_sensor.py 

Start Subscribers  
python subscribers/traffic_department.py  
python subscribers/health_department.py 
python subscribers/disaster_management.py  

Start Dashboard  
cd dashboard
python app.py  

Open browser: 
http://127.0.0.1:5000 

System Architecture

Sensors → MQTT Broker → Subscribers → Dashboard  

Future Enhancements
Real-time WebSocket updates
Mobile notifications
AI-based prediction system
Cloud deployment
Smart emergency response