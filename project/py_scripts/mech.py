import time
from machine import Pin, PWM
from servo import Servo

#Created the wheels 
class Wheels:
    def __init__(self):
        self.LWheel_pin = PWM(Pin(16)) 
        self.RWheel_pin = PWM(Pin(15))
        
        self.freq = 50
        self.min_us = 500
        self.max_us = 2500
        self.dead_zone_us = 1500
    
        self.__Lwheel = Servo(
            pwm = self.LWheel_pin, min_us=self.min_us, max_us=self.max_us, dead_zone_us=self.dead_zone_us, freq=self.freq)
        self.__Rwheel = Servo(
            pwm = self.RWheel_pin, min_us=self.min_us, max_us=self.max_us, dead_zone_us=self.dead_zone_us, freq=self.freq)
    
    def stop(self):
        self.__Lwheel.stop()
        self.__Rwheel.stop()
        time.sleep(3)
        #print('stop')
    
    def forward(self):
        self.__Lwheel.set_duty(1700)
        self.__Rwheel.set_duty(1300)
        #time.sleep(3)
        #print('going forward')
    
    def backward(self):
        self.__Lwheel.set_duty(750)
        self.__Rwheel.set_duty(2250)
        time.sleep(3)
        print('going back')
    

    def turnaround(self):
        self.__Rwheel.set_duty(1700)
        self.__Lwheel.set_duty(1700)
        #time.sleep(3)
        print('turn around')

    def turnleft(self):
        self.__Rwheel.set_duty(1350)
        self.__Lwheel.set_duty(1350)
        time.sleep(2.04)
        #print('turn left')
    
    def turnright(self):
        self.__Rwheel.set_duty(1650)
        self.__Lwheel.set_duty(1650)
        time.sleep(2.04)
        #print('turn right')

#Turned some to documentation to remove them from the code as it was not working in combo with ultrasonic sensor



#Tested the wheels her before having a proper unit test
wheels = Wheels()
while True:
    wheels.forward()


