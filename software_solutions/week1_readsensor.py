import time
from pyfirmata import Arduino, util
from os import system
# Set up the Arduino board
board = Arduino('/dev/cu.usbmodem14101') 

# Define the pin for the IR sensor
pin_ir_sensor = 1

# Set up the iterator for non-blocking reads
it = util.Iterator(board)
it.start()

# Configure the pin as an input
ir_sensor = board.get_pin('a:{0}:i'.format(pin_ir_sensor))

# Main loop
try:
    while True:
      
      system("clear")
      # Read the sensor value
      sensor_value = ir_sensor.read()

      # Check if an object is detected
      if sensor_value is not None and sensor_value < 0.04:
          print("Detected object")
      else:
          print("No object detected")
      
      # Wait for a short delay before the next reading
      time.sleep(0.1)

except KeyboardInterrupt:
    # Clean up the board on program exit
    board.exit()
