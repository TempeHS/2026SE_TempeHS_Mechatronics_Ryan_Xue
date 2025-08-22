from time import sleep
from PiicoDev_RGB import PiicoDev_RGB
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from RGB import RGBsensor

rgbsensor = RGBsensor()
while True: 
    rgbsensor.greenhue()
