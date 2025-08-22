from time import sleep
from PiicoDev_RGB import PiicoDev_RGB
from PiicoDev_VEML6040 import PiicoDev_VEML6040

class RGBsensor:
    def __init__(self):
        self.__sensor = PiicoDev_VEML6040()

    def greenhue(self):
        RGBSensor = self.__sensor.readHSV()
        hue = RGBSensor['hue']
        print(hue)
        if 80 < hue < 95: 
            return True
        else:
            print('No green')
        

#Succesfully had it working and showed when there was green paper
