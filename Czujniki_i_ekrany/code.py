import board, digitalio, time, displayio, busio, terminalio
from adafruit_display_text import label
from SoilSensor import SoilSensor
from Display import Display


kwiatek_1 = SoilSensor(board.A2)
display_1 = Display(board.GP26, board.GP27)
display_1.initialize()


display_1.dodaj_poletxt("czujnik_1", "Wilgotnosc_1:")
display_1.dodaj_poletxt("czujnik_2", "Wilgotnosc_2:")
display_1.dodaj_poletxt("czujnik_3", "Wilgotnosc_3:")


while True:
    display_1.zmien_zawartosc("czujnik_1", f"Wilgotnosc_1: {kwiatek_1.wilgotnosc()} %")
    time.sleep(1)



