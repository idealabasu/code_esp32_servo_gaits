from machine import Pin
from machine import PWM

import time
import math

# save the initial time in nanoseconds as t0
t0 = time.time_ns()

def get_seconds_float():
    '''
    This function accesses the internal time_ns() function and
    converts it to a floating point value in seconds
    '''
    # get current time, t in nanoseconds
    t = time.time_ns()
    # subtract from t0 to obtain the time since the program began
    dt = t-t0
    # convert to a float firsty, and then convert from nanoseconds
    # to seconds by multiplying by 10^9
    dt = float(dt)/1e9
    # return the change in time.
    return dt
    
def time_based_sinusoid(t,A,f,b,l0=0):
    '''
    convert the current time to a sinusoidal function
    with user-defined amplitude(A), frequency(f), DC offset (b),
    and time-based offset (l0) as a fraction of one period.
    '''
    y = A*(math.sin((2*(f*t-l0))*math.pi)) + b
    return y

class Servo(object):
    def __init__(self,pwm_pin, frequency=50,range_low_us=550, range_high_us=2400,pwm_bits = 10, input_range=180):
        self.frequency = frequency
        self.pwm_limit_low = range_low_us/1e6*frequency*(2**pwm_bits)
        self.pwm_limit_high = range_high_us/1e6*frequency*(2**pwm_bits)
        self.input_range = input_range
        # self.pwm = PWM(Pin(pwm_pin), self.frequency, resolution = pwm_bits)
        self.pwm = PWM(Pin(pwm_pin), self.frequency)

    def angle_to_pwm(self,degrees):
        '''
        this function converts a desired angle to
        its corresponding PWM value, using the range_low 
        and range_high constants defined inline
        '''
        # compute output scaling
        output_range = self.pwm_limit_high-self.pwm_limit_low
        # divide the desired angle by the input scaling, multiply
        #by the output scaling, and add the range_low value as an offset.
        output_pwm = ((degrees/self.input_range)*output_range)+self.pwm_limit_low
        # return the computed value as an integer
        return output_pwm

    def set_angle(self,angle):
        pwm = self.angle_to_pwm(angle)

        if pwm<self.pwm_limit_low:
            pwm = self.pwm_limit_low
        
        if pwm>self.pwm_limit_high:
            pwm = self.pwm_limit_high
        
        self.pwm.duty(int(pwm))
        

        