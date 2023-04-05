import busio, displayio, terminalio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
class Display():
    def __init__(self, SDA, SCL):
        self.SDA = SDA
        self.SCL = SCL
        self.pola_tekstowe = {}

    def dodaj_poletxt(self, nazwa, txt):
        miejsce = len(self.pola_tekstowe)
        print(miejsce)
        pole_txt = label.Label(terminalio.FONT, text=txt, color=0xFFFFFF, x=2, y=(miejsce+1)*10)
        self.pola_tekstowe[nazwa] = pole_txt
        self.splash.append(pole_txt)

    def zmien_zawartosc(self, nazwa, txt):
        self.pola_tekstowe[nazwa].text = txt

    def initialize(self):
        displayio.release_displays()
        I2C = busio.I2C(self.SCL, self.SDA)
        display_bus = displayio.I2CDisplay(I2C, device_address=0x3C)
        display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

        splash = displayio.Group()
        display.show(splash)

        color_bitmap = displayio.Bitmap(128, 64, 1)
        color_palette = displayio.Palette(1)
        color_palette[0] = 0xFFFFFF  # White

        bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
        splash.append(bg_sprite)

        ## Draw a smaller inner rectangle
        inner_bitmap = displayio.Bitmap(126, 62, 1)
        inner_palette = displayio.Palette(1)
        inner_palette[0] = 0x000000  # Black

        inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=1, y=1)
        splash.append(inner_sprite)
        self.splash = splash


