#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.messaging import BluetoothMailboxClient, TextMailbox
import time
# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

button = TouchSensor(Port.S2)
button2 = TouchSensor(Port.S4)

# Initiate the motors.
fw_motor = Motor(Port.A)
lr_motor = Motor(Port.B)

#forwardmin -39
#backwardmin 59
#leftmin -66
#rightmin 71
fw_motor.brake()

lr_motor.brake()


client = BluetoothMailboxClient()
forwardBack = TextMailbox("forwardBack",client)
leftRight = TextMailbox("leftRight",client)
upDown = TextMailbox("upDown",client)
client.connect("ev3dev")

while(True):
    if(fw_motor.angle()>15) :    
         forwardBack.send("forward")

    elif(fw_motor.angle()<-15) :
         forwardBack.send("backward")
    else:
         forwardBack.send("stopFB")

    if(lr_motor.angle()>20) :
         leftRight.send("left")

    elif(lr_motor.angle()<-20) :
         leftRight.send("right")
    else:
        leftRight.send("stopLR")

    if(button.pressed()):
        upDown.send("up")
    elif(button2.pressed()):
        upDown.send("down")
    else:
        upDown.send("noMove")
 
   