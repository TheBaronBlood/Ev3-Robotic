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

# PID-level-linefollower

def follow_line():
    left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)      #left_sensor port 1
    right_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)     #mid_sensor port 2
    left_sensor = ColorSensor(Port.S1)                          #right_sensor port 3
    right_sensor = ColorSensor(Port.S3)

    #BLACK = 10
    #WHITE = 60
    #threshole = int((WHITE - BLACK) / 2)
    
    PROPORTIONAL_GAIN = 4.2 # die Reaktionszeit wie schnell er auf den error reagieren soll
    
    INTEGRAL_GAIN = 0.008   # Addiert alle erros, und kann so bestimmen ob er noch auf der Linie ist oder nicht:
                            #   (Plus_error <- White L_refection Black -> Minus_error <- White R_refection Black -> Plus_error)
    
    DERIVATIVE_GAIN = 0.01  # Verschnellert oder Verlangsamt die Reationszeit je nach wie weit er von der Line Abweicht
                            #   (White -> high react, Black -> low react)

    integral = 0
    derivative = 0
    last_error = 0

    while True:
        L_refection = left_sensor.reflection()
        R_refection = right_sensor.reflection()
        error = L_refection - R_refection
        integral = integral + error 
        ev3.screen.clear()
        ev3.screen.draw_text(2,4,integral)
        print("Integral: ", integral)
        derivative = error - last_error
        turn = PROPORTIONAL_GAIN * error + INTEGRAL_GAIN * integral + DERIVATIVE_GAIN * derivative        
        right_motor.run(DRIVE_SPEED - turn)
        left_motor.run(DRIVE_SPEED + turn)
        last_error = error
       



while not any (ev3.buttons.pressed()):
        continue 

follow_line()
