from time import sleep
from PiicoDev_RGB import PiicoDev_RGB
from PiicoDev_VEML6040 import PiicoDev_VEML6040
from RGB import RGBsensor
from mech import Wheels

#Couldnt get this properly workng which resulted in navigation in not working
wheels = Wheels()
rgbsensor = RGBsensor()
while True: 
    if rgbsensor.greenhue():
        wheels.stop()
    else:
        wheels.forward()
