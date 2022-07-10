#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.messaging import BluetoothMailboxServer, TextMailbox

server = BluetoothMailboxServer()
forwardBack = TextMailbox('forwardBack' , server)
leftRight = TextMailbox('leftRight' , server)
upDown = TextMailbox('upDown' , server)

server.wait_for_connection()

forwardBack.wait()
leftRight.wait()
upDown.wait()


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

# Initiate the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
crane_motor = Motor(Port.C)

# Initiate the drive base.
#robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Go forward and backwards for one meter.
#robot.settings(500,1000,500,1000)

isStoppedLR = False
isStoppedFB = False


while(True):
    message = forwardBack.read()
    if(message=="forward") :
        #robot.straight(-100)
        left_motor.run(-1000)
        right_motor.run(-1000)
        isStoppedLR = False
        
    if(message=="backward") :
        #robot.straight(100)
        left_motor.run(1000)
        right_motor.run(1000)
        isStoppedLR = False
    
    if(message == "stopFB"):
        isStoppedLR = True

        ########################################################

    message = leftRight.read()

    if(message=="left") :
        #robot.turn(90)
        left_motor.run(1000)
        right_motor.run(0)
        isStoppedFB = False

    if(message=="right") :
        #robot.turn(-90)
        left_motor.run(0)
        right_motor.run(1000)
        isStoppedFB= False
    
    if(message=="stopLR") :
        #robot.turn(-90)
        isStoppedFB = True
        


        ########################################################

    if(isStoppedFB == True and isStoppedLR == True):
        left_motor.run(0)
        right_motor.run(0)

    

        ########################################################

    message = upDown.read()

    if(message=="up") :
        crane_motor.run(70)

    elif(message=="down") :
        crane_motor.run(-70)
    else:
        crane_motor.run(0)



