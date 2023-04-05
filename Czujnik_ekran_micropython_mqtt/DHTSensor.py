import json
from machine import Pin
from dht11 import DHT11, InvalidChecksum

class DHTSensor():
    def __init__(self, pin, pk):
        self.id = pk
        self.dht = DHT11(Pin(18, Pin.OUT))
    
    def read_temp(self):
       return  self.dht.temperature
    
    def read_hum(self):
       return  self.dht.humidity
    
    def prepare_json(self, temp):
        if temp:
           data = {
            "id":self.id,
            "name":"dht11",
            "measurement":self.read_temp(),
            "unit":"C"
            }
        else:
           data = {
            "id":self.id+2,
            "name":"dht11",
            "measurement":self.read_hum(),
            "unit":"%"
            }

        return json.dumps(data)
