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

# How To Run The Project

## Step 1 — Start MQTT Broker

```bash
mosquitto -v
```

---

## Step 2 — Start Publishers

### Traffic Publisher

```bash
python publishers/traffic_sensor.py
```

### Pollution Publisher

```bash
python publishers/pollution_sensor.py
```

### Weather Publisher

```bash
python publishers/weather_sensor.py
```

---

## Step 3 — Start Subscribers

### Traffic Department

```bash
python subscribers/traffic_department.py
```

### Health Department

```bash
python subscribers/health_department.py
```

### Disaster Management

```bash
python subscribers/disaster_management.py
```

---

## Step 4 — Start Dashboard

```bash
cd dashboard
python app.py
```

---

## Step 5 — Open Browser

```text
http://127.0.0.1:5000
```

---

# System Architecture

```text
Sensors
   ↓
MQTT Broker
   ↓
Subscribers
   ↓
Dashboard
```

---

# Future Enhancements

- AI-based prediction system
- Mobile notifications
- Cloud deployment
- Real-time WebSocket updates
- Smart emergency response
