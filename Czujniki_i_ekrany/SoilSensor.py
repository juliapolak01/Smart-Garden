from analogio import AnalogIn

class SoilSensor():
    def __init__(self, pin):
        self.pin = self.initialize(pin)

    def initialize(self, pin):
        return AnalogIn(pin)

    def get_voltage(self):
        return self.pin.value * 3.3/65536

    def wilgotnosc(self):
        return round((1 - self.get_voltage() / 3.3) * 100, 2)
