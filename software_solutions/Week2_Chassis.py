import time
from pyfirmata import ArduinoMega, PWM, OUTPUT

# Define the Chassis class to control the motors
class Chassis:
    def __init__(self, port):
        # Initialize the Arduino board with the specified port
        self.board = ArduinoMega(port)
        
        # Create a dictionary to store the motor pins
        self.motors = {"FR_forward": 22, "FR_reverse": 24, "FR_speed": 9,"FL_forward": 26,"FL_reverse": 28,"FL_speed": 10,"BR_forward": 5,"BR_reverse": 6,"BR_speed": 11,"BL_forward": 7,"BL_reverse": 8,"BL_speed" : 12}

    
    def FRmotor(self, direction: bool, speed: float):
        factor = 0
        motorForward = self.board.digital[self.motors_pin.get("FR_forward")] # one digitial output that controls direction
        motorReverse = self.board.digital[self.motor_pins.get("FR_reverse")] # second digital output that controls direction
        motorSpeed = self.board.digital[self.motor_pins.get("FR_speed")] # analog output that controls speed

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
        motorForward = self.board.digital[self.motor_pins.get("FL_forward")] # one digitial output that controls direction
        motorReverse = self.board.digital[self.motor_pins.get("FL_reverse")] # second digital output that controls direction
        motorSpeed = self.board.digital[self.motor_pins.get("FL_speed")] # analog output that controls speed

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
        motorForward = self.board.digital[self.motor_pins.get("BR_forward")] # one digitial output that controls direction
        motorReverse = self.board.digital[self.motor_pins.get("BR_reverse")] # second digital output that controls direction
        motorSpeed = self.board.digital[self.motor_pins.get("BR_speed")] # analog output that controls speed

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
        motorForward = self.board.digital[self.motor_pins.get("BL_forward")] # one digitial output that controls direction
        motorReverse = self.board.digital[self.motor_pins.get("BL_reverse")] # second digital output that controls direction
        motorSpeed = self.board.digital[self.motor_pins.get("BL_speed")] # analog output that controls speed

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
