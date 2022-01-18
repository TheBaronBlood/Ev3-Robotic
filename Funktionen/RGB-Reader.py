#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile, Font
from pybricks.iodevices import Ev3devSensor




# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


class RGB:

    def checkRGB(font_size=22, relodetime = 1):
        """ Gibt von Sonsor 1 und 3 die RGB farben in einer Tabelle auf dem Display aus 

        Arguments:
            font_size (int):
                Gibt die große der Schrift an 
            relodetime (int):
                Setzt die messungs pausen in Sekunden, Standard: 1 sec
            
        """
        screen = ev3.screen
        sl = Ev3devSensor(Port.S1) # setzt die Sensor Ports Links
        sr = Ev3devSensor(Port.S3) # setzt die Sensor Ports Rechts

        while True:
            # Liest die RGB werte aus und speichert sie in rl = RotLinks; gl = GrünLinks; bl = Blaulinks und 
            rl, gl, bl = sl.read('RGB-RAW')              # rr = RotRechts; gr = GrünRechts; br = BlauRechts
            rr, gr, br = sr.read('RGB-RAW')

            # Print results
            screen.set_font(Font(size=font_size)) # setzt die Schrift große 
            screen.draw_text(0, 10, 'Linker    Rechter')                  # Gibt die Werte 
            screen.draw_text(0, 40, 'R: {0}     R: {1}'.format(rl, rr))     # in einer "Tabelle"
            screen.draw_text(0, 65, 'G: {0}     G: {1}'.format( gl, gr,))   # unter ein ander 
            screen.draw_text(0, 90, 'B: {0}      B: {1}'.format(bl, br))   # aus :)
            wait(int(relodetime)*1000)
            screen.clear()  # Löscht den Screen sonnst würden die zahlen nach jedem WAIT über ein ander lappen 
            
            
            
