import json, requests
import paho.mqtt.client as mqtt
# http://www.emqx.io/online-mqtt-client#/recent_connections/2776d163-339b-4a8a-b2ff-ee3257de8ea9
# MQTT CONFIG
MQTT_SERVER = 'broker.emqx.io'
MQTT_PORT = 1883
MQTT_KEEPALIVE = 60
MQTT_USER = ''
MQTT_PASSWORD = ''


def on_connect(mqtt_client, userdata, flags, rc):
   if rc == 0:
       print('Connected successfully')
       mqtt_client.subscribe('konrad')
   else:
       print('Bad connection. Code:', rc)

def on_message(mqtt_client, userdata, msg):
    m_decode = str(msg.payload.decode("utf-8"))
    m_in = json.loads(m_decode)
    ## Tworzenie pomiaru do bazy danych
    url = "http://localhost:8000/"
    data = {
        "id":m_in["id"],
        "name":m_in["name"],
        "measurement":m_in["measurement"],
        "unit":m_in["unit"]
    }
    requests.post(url, data)



    ##     
    print(f'Received message on topic: {msg.topic} with payload: {msg.payload}')


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(MQTT_USER, MQTT_PASSWORD)
client.connect(
    host=MQTT_SERVER,
    port=MQTT_PORT,
    keepalive=MQTT_KEEPALIVE
)