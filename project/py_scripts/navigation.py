import time
from machine import Pin, PWM
from servo import Servo
from mech import Wheels
from ultrasonic import Ultrasonic

class Navigate:
    def __init__(self):
            self.__wheels = Wheels()
            self.__ultrasonic = Ultrasonic()
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

navigate = Navigate()
while True:
    navigate.movement()
