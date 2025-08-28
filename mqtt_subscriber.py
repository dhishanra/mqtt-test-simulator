import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
CLIENT_ID = "1111111111112222222222"
TOPIC = "topic/test"
USERNAME = "testd"
ACCESS_TOKEN = "37363130-dbe2-3293-8b97-31d14bbfc90e"

def on_connect(client, userdata, flags, rc):
    print("Connected with rc =", rc)
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    print("Received:", msg.payload.decode())

client = mqtt.Client(CLIENT_ID)
client.username_pw_set(USERNAME, ACCESS_TOKEN)
client.on_connect = on_connect
client.on_message = on_message
client.enable_logger()
client.connect(BROKER, PORT, keepalive=60)
client.loop_forever()
