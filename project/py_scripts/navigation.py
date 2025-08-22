import time
from machine import Pin, PWM
from mech import Wheels
from ultrasonic import Ultrasonic
from RGB import RGBsensor
from LCDscreen import LCD

#Created the main control system
#navigation worked succesfully but couldnt get good video sorry sir
class Navigate:
    def __init__(self):
            self.__wheels = Wheels()
            self.__ultrasonic = Ultrasonic()
            self.__rgb = RGBsensor()
            self.__lcd = LCD()
            #self.__side_wall, self.__front_clear = self.__ultrasonic.wallL()
            #self.__side_wall, self.__front_wall = self.__ultrasonic.wallFL()

    def movement(self):
        self.__ultrasonic.print_distance()
        if self.__ultrasonic.obstacleahead():
            self.__wheels.stop()
            if self.__ultrasonic.wallFL():
                self.__wheels.turnright()
            else:

                self.__wheels.turnleft()
        else:
            self.__wheels.forward()

#tried implementing the LCD and RGB but was not succesful
    def LCDRGB(self):
        if self.__rgb.greenhue():
            self.__lcd.LCDscreen()
            self.__wheels.stop()
            time.sleep(1)
            self.__wheels.forward()
        else:
            self.__lcd.LCDSCREEN()


navigate = Navigate()
while True:
    navigate.movement()
    navigate.LCDRGB()
