from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms
from RGB import RGBsensor

#Attempted to create LCD screen
class LCD():
    def __init__ (self):
        self.__display = create_PiicoDev_SSD1306()

    def LCDscreen(self):
        self.__display.fill(0)
        self.__display.text('colour: ',30,20, 1)
        self.__display.text('green',50,35, 1)
        self.__display.show()

    def LCDSCREEN(self):
        self.__display.fill(0)
        self.__display.text('No colour',30,20, 1)
        self.__display.show()

#Succesfully had LCD showing the functions
lcdscreen = LCD()
while True:
    lcdscreen.LCDscreen()       

