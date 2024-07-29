#import all the libraries
# from machine import Pin
# from machine import PWM
import math
import time
import my_servo
import uasyncio as asyncio
from my_servo import Servo

f = .5
A = 90
b = 90

l1 = 0
l2 = .25
l3 = .5
l4 = .75

# create a new PWM instance and call it servo1
servo1 = my_servo.Servo(13)
servo2 = my_servo.Servo(12)
servo3 = my_servo.Servo(14)
servo4 = my_servo.Servo(27)

def update_servos():
    # time.sleep is not as necessary...can be commented
    # out except if you want to print values out.
    # time.sleep(.01)
    
    # get the current time in (floating-point) seconds
    t = my_servo.get_seconds_float()

    # compute the desired angle for servo 1
    y1 = my_servo.time_based_sinusoid(t,A,f,b,l1)
    y2 = my_servo.time_based_sinusoid(t,A,f,b,l2)
    y3 = my_servo.time_based_sinusoid(t,A,f,b,l3)
    y4 = my_servo.time_based_sinusoid(t,A,f,b,l4)

    # print out the desired angle.  Not essential, can be commented out
    # print(y1)

    # set servo 1 pwm value according to the desired angle
    servo1.set_angle(y1)
    servo2.set_angle(y2)
    servo3.set_angle(y3)
    servo4.set_angle(y4)
    

async def update_servo_loop():
    ii = 0
    while True:
        # print(ii)
        ii+=1
        update_servos()
        await asyncio.sleep(0.1)
