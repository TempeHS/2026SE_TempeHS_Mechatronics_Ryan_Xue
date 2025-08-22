import time
from machine import Pin, PWM
from ultrasonic import Ultrasonic
from mech import Wheels

#created unit test for US sensor and worked
ultrasonic = Ultrasonic()
wheels = Wheels()

while True:
    ultrasonic.print_distance()
    wheels.forward()
    if ultrasonic.obstacleahead():
        wheels.turnleft()
    
    