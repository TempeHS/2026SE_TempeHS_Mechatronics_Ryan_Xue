from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms
from RGB import RGBsensor
from LCDscreen import LCD

#simple unit test for LCD screen
lcd = LCD()
while True:
    lcd.LCDscreen()
