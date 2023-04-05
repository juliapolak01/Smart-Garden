import network, time
from umqtt.simple import MQTTClient
from SoilSensor import SoilSensor
from Display import Display
from DHTSensor import DHTSensor

dht = DHTSensor(18, 4)
czujnik_1 = SoilSensor(28, 1)
czujnik_2 = SoilSensor(27, 2)
czujnik_3 = SoilSensor(26, 3)
display = Display(16, 17)

# http://www.hivemq.com/demos/websocket-client/?
NAME = "FunBox2-041D"
PASSWORD = "CEC2DD53E916A43D166443ED61" # Tutaj trzeba zmienic pod siebie

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(NAME, PASSWORD)

time.sleep(10)

mqtt_server = "broker.emqx.io"
client_id = "kaczorDonald123"

def mqtt_connect():
    client = MQTTClient(client_id, mqtt_server, keepalive=3600)
    client.connect()
    print('Connected to %s MQTT Broker'%(mqtt_server))
    return client

def reconnect():
   print('Failed to connect to the MQTT Broker. Reconnecting...')
   time.sleep(5)
   machine.reset()
   
try:
    client = mqtt_connect()
except OSError as e:
    reconnect()
   
topic_pub = b'konrad'


   
while True:
    #Wyswietlanie na ekranie 
    display.clear_screen()
    display.display_text("Czujnik 1 {} %".format(czujnik_1.read_humidity()), 0, 0)
    display.display_text("Czujnik 2 {} %".format(czujnik_2.read_humidity()), 0, 10)
    display.display_text("Czujnik 3 {} %".format(czujnik_3.read_humidity()), 0, 20)
    display.display_text("Temperatura {} C".format(dht.read_temp()), 0, 30)
    display.display_text("Wilgotnosc {} %".format(dht.read_hum()), 0, 40)
    display.show()
    
    
    topic_msg1 = czujnik_1.prepare_json()
    topic_msg2 = czujnik_2.prepare_json()
    topic_msg3 = czujnik_3.prepare_json()
    topic_msg4 = dht.prepare_json(True)
    topic_msg5 = dht.prepare_json(False)
    
    client.publish(topic_pub, topic_msg1)
    time.sleep(10)
    client.publish(topic_pub, topic_msg2)
    time.sleep(10)
    client.publish(topic_pub, topic_msg3)
    time.sleep(10)
    client.publish(topic_pub, topic_msg4)
    time.sleep(10)
    client.publish(topic_pub, topic_msg5)
    time.sleep(10)
 


