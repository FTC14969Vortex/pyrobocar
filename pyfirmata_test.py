from pyfirmata import ArduinoMega
import time

board = ArduinoMega("/dev/cu.usbmodem14101")

#List of the pin number for every value (Forward, Reverse, Speed) of each motor

pin_dict = {}

pin_dict["MEGA"] = {"FR_forward": 22,
                       "FR_reverse": 24,
                       "FR_speed": 9,
                       "FL_forward": 26,
                       "FL_reverse": 28,
                       "FL_speed": 10,
                       "BR_forward": 5,
                       "BR_reverse": 6,
                       "BR_speed": 11,
                       "BL_forward": 7,
                       "BL_reverse": 8,
                       "BL_speed" : 12}

pin_dict["UNO"] = {"LeftSide_speed": 9,
                   "LeftSide_forward": 11,
                   "LeftSide_reverse": 12,
                   "RightSide_speed": 6,
                   "RightSide_forward": 8,
                   "RightSide_reverse": 7}

def FRmotor(robot_type: str, direction: bool, speed:float):
    if (robot_type == 'MEGA'): 
        motorForward = board.digital[pin_dict["MEGA"].get("FR_forward")] # one digitial output that controls direction
        motorReverse = board.digital[pin_dict["MEGA"].get("FR_reverse")] # second digital output that controls direction
        motorSpeed = board.digital[pin_dict["MEGA"].get("FR_speed")] # analog output that controls speed

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

def FLmotor(robot_type: str, direction: bool, speed:float):
    if (robot_type == 'MEGA'): 
        motorForward = board.digital[pin_dict["MEGA"].get("FL_forward")] # one digitial output that controls direction
        motorReverse = board.digital[pin_dict["MEGA"].get("FL_reverse")] # second digital output that controls direction
        motorSpeed = board.digital[pin_dict["MEGA"].get("FL_speed")] # analog output that controls speed

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
        
def BRmotor(robot_type: str, direction: bool, speed:float):
    if (robot_type == 'MEGA'): 
        motorForward = board.digital[pin_dict["MEGA"].get("BR_forward")] # one digitial output that controls direction
        motorReverse = board.digital[pin_dict["MEGA"].get("BR_reverse")] # second digital output that controls direction
        motorSpeed = board.digital[pin_dict["MEGA"].get("BR_speed")] # analog output that controls speed

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
        
def BLmotor(robot_type: str, direction: bool, speed:float):
    if (robot_type == 'MEGA'): 
        motorForward = board.digital[pin_dict["MEGA"].get("BL_forward")] # one digitial output that controls direction
        motorReverse = board.digital[pin_dict["MEGA"].get("BL_reverse")] # second digital output that controls direction
        motorSpeed = board.digital[pin_dict["MEGA"].get("BL_speed")] # analog output that controls speed

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
    FRmotor("MEGA", True, 0)
    BRmotor("MEGA", True, 0)
    FLmotor("MEGA", True, 0)
    BLmotor("MEGA", True, 0)


FRmotor("MEGA", True, 1)
BRmotor("MEGA", True, 1)
FLmotor("MEGA", True, 1)
BLmotor("MEGA", True, 1)
time.sleep(5)
StopMotors()

# while True:
#     board.digital[13].write(1)
#     time.sleep(0.5)
#     board.digital[13].write(0)
#     time.sleep(0.5)






