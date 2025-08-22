import time
from machine import Pin, PWM
from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms
from mech import Wheels

class Ultrasonic:
    def __init__(self):
        self.front_sensor = PiicoDev_Ultrasonic(id=[0, 0, 1, 0])
        self.side_sensor = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])

    def distance(self):
        return self.front_sensor.distance_mm, self.side_sensor.distance_mm
    
    def print_distance(self):
        front, side = self.distance()
        print(f'{front}, {side}')
        sleep_ms(100)
    

    def obstacleahead(self):
        front = self.front_sensor.distance_mm
        #print(f'{front}')
        if front < 50:
            return True
    
    def wallL(self):
        side = self.side_sensor.distance_mm
        front = self.front_sensor.distance_mm
        #print(f'{side}')
        return side > 50
    
    def wallFL(self):
        side = self.side_sensor.distance_mm
        front = self.front_sensor.distance_mm
        return side < 50





#while True:
#    front, side = ultrasonic.distance()
#    print(f'{front}, {side}')
#    ultrasonic.print_distance()
#    if ultrasonic.obstacleahead():
#        if side_wall and front_clear:
#            wheels.turnleft()
#    else:
#        wheels.forward()

    
    