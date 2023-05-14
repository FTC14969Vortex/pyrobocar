from pyfirmata import ArduinoMega
import time

board = ArduinoMega("/dev/cu.usbmodem14201")


motorFRpos = board.digital[22] # one digitial output that controls direction
motorFRneg = board.digital[24] # second digital output that controls direction
motorFRspeed = board.digital[9] # analog output that controls speed

motorFRspeed.mode = 3
motorFRpos.mode = 1
motorFRneg.mode = 1

motorFRpos.write(1)
motorFRneg.write(0)
motorFRspeed.write(0.75)

time.sleep(5)

motorFRspeed.write(0)

# while True:
#     board.digital[13].write(1)
#     time.sleep(0.5)
#     board.digital[13].write(0)
#     time.sleep(0.5)






