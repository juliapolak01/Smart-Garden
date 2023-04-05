from ssd1306 import SSD1306_I2C
from oled import Write, GFX, SSD1306_I2C
from machine import Pin, ADC, I2C
from oled.fonts import ubuntu_mono_12

class Display():
    def __init__(self, SDA, SCL):
        WIDTH = 128
        HEIGHT = 64
        self.oled = SSD1306_I2C(WIDTH, HEIGHT, I2C(0, scl=Pin(SCL), sda=Pin(SDA)))
        self.font = Write(self.oled, ubuntu_mono_12)
    
    def clear_screen(self):
        self.oled.fill(0)
       
    def display_text(self, text, x, y):
        self.font.text(text, x, y, 1)
    
    def show(self):
        self.oled.show()
    
