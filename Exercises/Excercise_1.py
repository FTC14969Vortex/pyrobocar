from pyfirmata import ArduinoMega
import time

board = ArduinoMega("/dev/cu.usbmodem14201")

#List of the pin number for every value (Forward, Reverse, Speed) of each motor

pin_dict = {}

pin_dict = {"FR_forward": 22, "FR_reverse": 24, "FR_speed": 9,"FL_forward": 26,"FL_reverse": 28,"FL_speed": 10,"BR_forward": 5,"BR_reverse": 6,"BR_speed": 11,"BL_forward": 7,"BL_reverse": 8,"BL_speed" : 12}

def FRmotor(direction: bool, speed: float):
    motorForward = board.digital[pin_dict.get("FR_forward")] # one digitial output that controls direction
    motorReverse = board.digital[pin_dict.get("FR_reverse")] # second digital output that controls direction
    motorSpeed = board.digital[pin_dict.get("FR_speed")] # analog output that controls speed

    motorSpeed.mode = 3
    motorForward.mode = 1
    motorReverse.mode = 1

    if (direction == True) :
        motorForward.write(1)
        motorReverse.write(0)
        
    elif (direction == False):
        motorForward.write(0)
        motorReverse.write(1)
    
    motorSpeed.write(speed)

def FLmotor(direction: bool, speed:float):
    motorForward = board.digital[pin_dict.get("FL_forward")] # one digitial output that controls direction
    motorReverse = board.digital[pin_dict.get("FL_reverse")] # second digital output that controls direction
    motorSpeed = board.digital[pin_dict.get("FL_speed")] # analog output that controls speed

    motorSpeed.mode = 3
    motorForward.mode = 1
    motorReverse.mode = 1

    if (direction == True) :
        motorForward.write(1)
        motorReverse.write(0)
        
    elif (direction == False):
        motorForward.write(0)
        motorReverse.write(1)
    
        motorSpeed.write(speed)
        
def BRmotor(direction: bool, speed:float):
    motorForward = board.digital[pin_dict.get("BR_forward")] # one digitial output that controls direction
    motorReverse = board.digital[pin_dict.get("BR_reverse")] # second digital output that controls direction
    motorSpeed = board.digital[pin_dict.get("BR_speed")] # analog output that controls speed

    motorSpeed.mode = 3
    motorForward.mode = 1
    motorReverse.mode = 1

    if (direction == True) :
        motorForward.write(1)
        motorReverse.write(0)
        
    elif (direction == False):
        motorForward.write(0)
        motorReverse.write(1)
    
    motorSpeed.write(speed)
        
def BLmotor(direction: bool, speed:float):
        motorForward = board.digital[pin_dict.get("BL_forward")] # one digitial output that controls direction
        motorReverse = board.digital[pin_dict.get("BL_reverse")] # second digital output that controls direction
        motorSpeed = board.digital[pin_dict.get("BL_speed")] # analog output that controls speed

        motorSpeed.mode = 3
        motorForward.mode = 1
        motorReverse.mode = 1

        if (direction == True) :
            motorForward.write(1)
            motorReverse.write(0)
            
        elif (direction == False):
            motorForward.write(0)
            motorReverse.write(1)
        
        motorSpeed.write(speed)
        
def StopMotors():
    FRmotor(True, 0)
    BRmotor(True, 0)
    FLmotor(True, 0)
    BLmotor(True, 0)


#Move Front Right Motor
FRmotor(True,1)
time.sleep(1)
StopMotors()
time.sleep(0.3)
FRmotor(False,1)
time.sleep(1)
StopMotors()
time.sleep(0.3)

#Move Front Left Motor
FLmotor(True,1)
time.sleep(1)
StopMotors()
time.sleep(0.3)
FLmotor(False,1)
time.sleep(1)
StopMotors()
time.sleep(0.3)

#Move Back Left Motor
BLmotor(True,1)
time.sleep(1)
StopMotors()
time.sleep(0.3)
BLmotor(False,1)
time.sleep(1)
StopMotors()
time.sleep(0.3)

#Move Back Right Motor
BRmotor(True,1)
time.sleep(1)
StopMotors()
time.sleep(0.3)
BRmotor(False,1)
time.sleep(1)
StopMotors()
time.sleep(0.3)



