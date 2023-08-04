import time
from pyfirmata import ArduinoMega, PWM, OUTPUT

# Define the Chassis class to control the motors
class Chassis:
    def __init__(self, port,):
        # Initialize the Arduino board with the specified port
        self.board = ArduinoMega(port)
        
        # Create a dictionary to store the motor pins
        self.motors = {"FR_forward": 22, "FR_reverse": 24, "FR_speed": 9,"FL_forward": 26,"FL_reverse": 28,"FL_speed": 10,"BR_forward": 5,"BR_reverse": 6,"BR_speed": 11,"BL_forward": 7,"BL_reverse": 8,"BL_speed" : 12}

    
    def FRmotor(self, direction: bool, speed: float):
        factor = 0
        motorForward = self.board.digital[self.motors.get("FR_forward")] # one digitial output that controls direction
        motorReverse = self.board.digital[self.motors.get("FR_reverse")] # second digital output that controls direction
        motorSpeed = self.board.digital[self.motors.get("FR_speed")] # analog output that controls speed

        motorSpeed.mode = PWM
        motorForward.mode = OUTPUT
        motorReverse.mode = OUTPUT

        if (direction == True) :
            motorForward.write(1)
            motorReverse.write(0)
            
        elif (direction == False):
            motorForward.write(0)
            motorReverse.write(1)
        
        motorSpeed.write(speed)

    def FLmotor(self, direction: bool, speed:float):
        motorForward = self.board.digital[self.motors.get("FL_forward")] # one digitial output that controls direction
        motorReverse = self.board.digital[self.motors.get("FL_reverse")] # second digital output that controls direction
        motorSpeed = self.board.digital[self.motors.get("FL_speed")] # analog output that controls speed

        motorSpeed.mode = PWM
        motorForward.mode = OUTPUT
        motorReverse.mode = OUTPUT

        if (direction == True) :
            motorForward.write(1)
            motorReverse.write(0)
            
        elif (direction == False):
            motorForward.write(0)
            motorReverse.write(1)
        
        motorSpeed.write(speed)
            
    def BRmotor(self, direction: bool, speed:float):
        motorForward = self.board.digital[self.motors.get("BR_forward")] # one digitial output that controls direction
        motorReverse = self.board.digital[self.motors.get("BR_reverse")] # second digital output that controls direction
        motorSpeed = self.board.digital[self.motors.get("BR_speed")] # analog output that controls speed

        motorSpeed.mode = PWM
        motorForward.mode = OUTPUT
        motorReverse.mode = OUTPUT

        if (direction == True) :
            motorForward.write(1)
            motorReverse.write(0)
            
        elif (direction == False):
            motorForward.write(0)
            motorReverse.write(1)
        
        motorSpeed.write(speed)
        
    def BLmotor(self, direction: bool, speed:float):
        motorForward = self.board.digital[self.motors.get("BL_forward")] # one digitial output that controls direction
        motorReverse = self.board.digital[self.motors.get("BL_reverse")] # second digital output that controls direction
        motorSpeed = self.board.digital[self.motors.get("BL_speed")] # analog output that controls speed

        motorSpeed.mode = PWM
        motorForward.mode = OUTPUT
        motorReverse.mode = OUTPUT

        if (direction == True) :
            motorForward.write(1)
            motorReverse.write(0)
            
        elif (direction == False):
            motorForward.write(0)
            motorReverse.write(1)
        
        motorSpeed.write(speed)
    
    def StopMotors(self):
        self.FRmotor(True, 0)
        self.BRmotor(True, 0)
        self.FLmotor(True, 0)
        self.BLmotor(True, 0)
    
    def moveForward(self, speed: float):
        self.FRmotor(True, speed)
        self.FLmotor(True, speed)
        self.BRmotor(True, speed)
        self.BLmotor(True, speed)
        
    def moveBackward(self, speed: float):
        self.FRmotor(False, speed)
        self.FLmotor(False, speed)
        self.BRmotor(False, speed)
        self.BLmotor(False, speed)

    def moveLeft(self, speed: float):
        self.FRmotor(True, speed)
        self.FLmotor(False, speed)
        self.BRmotor(False, speed)
        self.BLmotor(True, speed)

    def moveRight(self, speed: float):
        self.FRmotor(False, speed)
        self.FLmotor(True, speed)
        self.BRmotor(True, speed)
        self.BLmotor(False, speed)
        
    def turnLeft(self, speed: float):
        self.FRmotor(True, speed)
        self.FLmotor(False, speed)
        self.BRmotor(True, speed)
        self.BLmotor(False, speed)

    def turnRight(self, speed: float):
        self.FRmotor(False, speed)
        self.FLmotor(True, speed)
        self.BRmotor(False, speed)
        self.BLmotor(True, speed)
   
    def moveDR(self):
        self.FRmotor(False, 0)
        self.FLmotor(True, 1)
        self.BRmotor(True, 0.5)
        self.BLmotor(False, 0)

    def moveDL(self):
        self.FRmotor(True, 1)
        self.FLmotor(False, 1)
        self.BRmotor(False, 1)
        self.BLmotor(True, 1)

#Use the Class to program your robot.
#Make it move in the following shapes:

# Square
# Rectangle
# Triangle
# Pentagon
# Hexagon
# U - Shape
# Circle
# Star
# Hebrew Star
# Heart
# Decagon
# Your Initials
# Oval

#BONUS

#Map of Europe
#Self Portrait
