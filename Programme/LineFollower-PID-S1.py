#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.
# Quelle: http://www.inpharmix.com/jps/PID_Controller_For_Lego_Mindstorms_Robots.html
#         https://thecodingfun.com/2020/06/16/lego-mindstorms-ev3-pid-line-follower-code-by-using-micropython-2-0/

# Create your objects here.
ev3 = EV3Brick()

BLACK = 0
WHITE = 0

DRIVE_SPEED = 125
ev3.speaker.set_volume(5)


# mid_sensor port 3
#left_sensor port 2
#right_sensor port 4

# read the values for the line following
def calibration():
    color_sensor = ColorSensor(Port.S2)
    while not any (ev3.buttons.pressed()):
        continue
    wait(1000)
    white_color = color_sensor.reflection()
    ev3.speaker.beep()
    print("white color: ", white_color)
    

    while not any(ev3.buttons.pressed()):
        continue
    wait(1000)
    black_color = color_sensor.reflection()
    ev3.speaker.beep()
    print("black color: ", black_color)
    
    result = []
 
    result.append(white_color)
    result.append(black_color)

    return result
   

# 3-level-follower

def follow_line(WHITE , BLACK):
    left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    right_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
    mid_sensor = ColorSensor(Port.S2)

    #BLACK = 10
    #WHITE = 60
    threshole = int((WHITE - BLACK) / 2)
    PROPORTIONAL_GAIN = 6
    INTEGRAL_GAIN = 0.002
    DERIVATIVE_GAIN = 0.020

    integral = 0
    derivative = 0
    last_error = 0

    while True:
        mrefection = mid_sensor.reflection()
        error = mrefection - threshole 
        integral = integral + error 
        derivative = error - last_error
        turn = PROPORTIONAL_GAIN * error + INTEGRAL_GAIN * integral + DERIVATIVE_GAIN * derivative        
        right_motor.run(DRIVE_SPEED - turn)
        left_motor.run(DRIVE_SPEED +turn)
        last_error = error
       

values = []


values = calibration()
follow_line(values[0], values[1])
