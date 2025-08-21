import time
from machine import Pin, PWM
from ultrasonic import Ultrasonic
from mech import Wheels

ultrasonic = Ultrasonic()
wheels = Wheels()

while True:
    ultrasonic.print_distance()
    if ultrasonic.obstacleahead():
        wheels.turnleft
    else:
        wheels.forward
