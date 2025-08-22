from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms
from RGB import RGBsensor

class LCD():
    def __init__ (self):
        self.__display = create_PiicoDev_SSD1306()

    def LCDscreen(self):
        for counter in range(0,101):
            self.__display.fill(0)
            self.__display.text('colour: ',30,20, 1)
            self.__display.text('green',50,35, 1)
            self.__display.show()


lcdscreen = LCD()
while True:
    lcdscreen.LCDscreen       