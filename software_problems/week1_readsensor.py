#PYFIRMATA DOCUMENTATION: https://pyfirmata.readthedocs.io/en/latest/genindex.html

#Import all the libraries you will be using to control your robot
import time
from pyfirmata import ArduinoMega, util


#Set up the Arduino board by defining the serial port that USB is plugged into

board = ArduinoMega('') #Serial port here

# Since we are using an analog pin, we need to start and iterator thread.
#Without this, the analog pin would keep sending information until the board overloads.
#This command essentially refreshes the pin
it = util.Iterator(board)
it.start()

#Get the pin from the board using and store it in a variable
#MAKE SURE: That the sensor is configured as a analog pin and is used as an input.
#TIP: Hover your cursor over any method to check the documentation for the format you should use. 

#CODE HERE

#In the robot's update loop read the sensor and print the value
#Also add print statement for if the object is/isn't detected

#Wait for a 0.1 seconds before the next reading, because the pin needs time to update.

#CODE HERE