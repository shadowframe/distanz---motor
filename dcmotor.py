# MicroPython dcmotor driver

import utime
from machine import Pin

# motor left pin layout
motor1a = Pin(10, Pin.OUT)
motor1b = Pin(11, Pin.OUT)
# motor right pin layout
motor2a = Pin(13, Pin.OUT)
motor2b = Pin(12, Pin.OUT)

'''
Single Motor functions
'''


# motor left functions


def forward_left():
    motor1a.high()
    motor1b.low()


def backward_left():
    motor1a.low()
    motor1b.high()


def stop_left():
    motor1a.low()
    motor1b.low()


# motor right functions
def forward_right():
    motor2a.high()
    motor2b.low()


def backward_right():
    motor2a.low()
    motor2b.high()


def stop_right():
    motor2a.low()
    motor2b.low()


# all engines forward, backward, stop


def forward():
    forward_left()
    forward_right()


def backward():
    backward_left()
    backward_right()


def motor_stop():
    stop_left()
    stop_right()


def left():
    backward_left()
    forward_right()


def right():
    forward_left()
    backward_right()


# test motor left

def start_test():
    print("forward_left")
    forward_left()
    utime.sleep(2)
    print("backward_left")
    backward_left()
    utime.sleep(2)
    stop_left()

    print("forward_right")
    forward_right()
    utime.sleep(2)
    print("backward_right")
    backward_right()
    utime.sleep(2)
    stop_right()

    print("forward")
    forward()
    utime.sleep(4)
    motor_stop()

    print("backward")
    backward()
    utime.sleep(4)
    motor_stop()

    print("left")
    left()
    utime.sleep(4)
    motor_stop()

    print("right")
    right()
    utime.sleep(4)
    motor_stop()

# for i in range(2):
#     start_test()
