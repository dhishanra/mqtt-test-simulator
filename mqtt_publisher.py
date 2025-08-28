#!/usr/bin/env python

import time
import paho.mqtt.client as mqtt
import uuid

unique_number = str(uuid.uuid4().int)[-6:] 
# for i in {1..10}; do python3 mqtt_publisher.py & done

# ================================================
# Configurations
# ===============================================
BROKER = "localhost"   
PORT = 1883                    
USERNAME = "test"  #any        
ACCESS_TOKEN = "37363130-dbe2-3293-8b97-31d14bbfc90e"              
CLIENT_ID = f"dra-pub-{unique_number}"
TOPIC_TO_PUBLISH = "topic/test"
# ===============================================
REPEATING_COUNT=5
REPEATING_TIME=5  #seconds
KEEP_ALIVE=60  #Client must send data at least once every 60s, otherwise broker disconnects.
MESSAGE= f"HELLO from {CLIENT_ID}"
QOS=0    # 0=At most once, 1=At least once, 2=Exactly once
RETAIN=True  #new subscribers can see last msg on broker

# ==============================
# MQTT Callbacks
# ==============================
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to broker")
    else:
        print("Connection failed", rc)

def on_publish(client, userdata, mid):
    print("Message published successfully (mid: {})".format(mid))

# ==============================
# Main
# ==============================
def main():
    mqttClient = mqtt.Client(client_id=CLIENT_ID)
    mqttClient.on_connect = on_connect
    mqttClient.on_publish = on_publish

    # If broker requires username/password
    mqttClient.username_pw_set(USERNAME, ACCESS_TOKEN)

    print(f"Connecting to MQTT Broker {BROKER}:{PORT}")
    mqttClient.connect(BROKER, PORT, keepalive=KEEP_ALIVE)

    mqttClient.loop_start()

    # Publish messages
    for i in range(REPEATING_COUNT):
        message = f"{MESSAGE} {i+1}"
        print("Publishing:", message)
        mqttClient.publish(TOPIC_TO_PUBLISH, message, qos=QOS, retain=RETAIN)
        time.sleep(REPEATING_TIME)

    mqttClient.loop_stop()
    mqttClient.disconnect()
    print("Disconnected from broker")

if __name__ == '__main__':
    main()
