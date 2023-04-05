from machine import Pin, ADC
import json


class SoilSensor():
    def __init__(self, pin, pk):
        self.pin = ADC(pin)
        self.id = pk

    def get_voltage(self):
        return self.pin.read_u16() * 3.3/65536

    def read_humidity(self):
        return round((1 - self.get_voltage() / 3.3) * 100, 2)
    
    def prepare_json(self):
        data = {
            "id":self.id,
            "name":"czujnik",
            "measurement":self.read_humidity(),
            "unit":"%"
            }
        return json.dumps(data)


