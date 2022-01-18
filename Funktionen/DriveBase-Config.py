#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.iodevices import Ev3devSensor
from pybricks.tools import wait
from pybricks.media.ev3dev import Font # oder an > from pybricks.media.ev3dev import SoundFile, ImageFile < noch , Font dran hängen


ev3 = EV3Brick()

right_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)

left_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)

robot=DriveBase(left_motor, right_motor,wheel_diameter=31.5, axle_track=150)

robot.straight(1000)

robot.turn(-90)

#robot.drive(360, 360)
