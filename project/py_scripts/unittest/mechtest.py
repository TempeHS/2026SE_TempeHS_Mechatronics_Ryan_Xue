import time
from machine import Pin, PWM
from mech import Wheels


#Unit tested each function for wheels
wheels = Wheels()
while True:
    wheels.forward()
    wheels.backward()
    wheels.turnleft()
    wheels.turnright()
    wheels.stop

