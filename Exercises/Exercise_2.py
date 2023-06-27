from pyfirmata import ArduinoMega, SERVO
import time

board = ArduinoMega("/dev/cu.usbmodem14201")

board.digital[13].mode = SERVO

def rotateServo(angle):
    board.digital[13].write(angle)
    
while True:
    rotateServo(0)
    time.sleep(0.5)
    rotateServo(360)
    time.sleep(0.5)
    rotateServo(0)