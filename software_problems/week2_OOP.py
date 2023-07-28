import time
from pyfirmata import ArduinoMega, PWM, OUTPUT

# Create and define the Chassis class to control the motors
class NameHere:
    def __init__(self, port):
        
        # Initialize the Arduino board with the specified port, like you have done in the past.
        #MAKE SURE: When you create your class object define the port in the parenthesis as it is being referenced here
        self.board = ArduinoMega(port)
        
        # Create a dictionary to store the motor pins
        self.motors = {"FR_forward": 22, "FR_reverse": 24, "FR_speed": 9,"FL_forward": 26,"FL_reverse": 28,"FL_speed": 10,"BR_forward": 5,"BR_reverse": 6,"BR_speed": 11,"BL_forward": 7,"BL_reverse": 8,"BL_speed" : 12}

    #Create methods to control the robot motors. The first one has been started for you. 
    def FRmotor(self, direction: bool, speed: float):
        #  This method has two parameters: `direction` (a boolean) and `speed` (a float).
            # `direction` will determine the movement direction of that motor: True for forward and False for backward/stop.
            # `speed` will control the motor speed using a float value.

        # Inside the method, you'll need to:
            #Create and define a variable for the forward pin, reverse pin, and speed pin of the motor.
            #Configure the direction pins as digital outputs and the speed pin digital PWM.
            #The first one has been done for you as an example (below):
        motorForward = self.board.digital[self.motors.get("FR_forward")] # one digitial output that controls direction


        # Implement the logic to set the motor direction and speed based on the provided `direction` and `speed` parameters.
            # If `direction` is True, set the motor to move forward.
            # If `direction` is False, stop or reverse the motor.

        #Finally, write the `speed` value to the motorSpeed analog output to control the motor's speed. 
        #Repeat the same process for all other motors
   
        #CODE HERE
   
   
#Create methods to move the robot in different directions. (Ex. forward, backward, left, right, turning)
#You will need to control the motors based on the direction (True/Flase) and speed. Below we have an example with instructoins for the first method. 
   
    def moveForward(self, speed: float):
        #Implement the movement logic for moving the robot forward.
        #Use the self.FRmotor, self.FLmotor, self.BRmotor, and self.BLmotor methods to control the motors and their speed.

  
        #Now create a method to stop the movement of the robot. 
    
    #Once you have finished defining all the methods, write some simple Autonomous code to move the car in a square!
    #Before you write the Auto code, make sure you have created a new variable and assigned the value of your class (and the port argument).
    #By assigning your class to the new variable, this variable now represents an object which can control the motors of the robot, and access methods that were defined in your class
    #Once you are done making your robot move in a square, you can program any other pattern of movement you would like.