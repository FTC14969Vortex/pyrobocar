from pyfirmata import ArduinoMega
import pygame

#Set up board port
board = ArduinoMega("/dev/cu.usbmodem14101")

#Init pygame and pygame screen
pygame.init
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Robot Controller")

#List of the pin number for every value (Forward, Reverse, Speed) of each motor
pin_dict = {}
pin_dict = {"FR_forward": 22, "FR_reverse": 24, "FR_speed": 9,"FL_forward": 26,"FL_reverse": 28,"FL_speed": 10,"BR_forward": 5,"BR_reverse": 6,"BR_speed": 11,"BL_forward": 7,"BL_reverse": 8,"BL_speed" : 12}

#Methods for motors and movement
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
    
def moveForward(speed: float):
    FRmotor(True, speed)
    FLmotor(True, speed)
    BRmotor(True, speed)
    BLmotor(True, speed)
    
def moveBackward(speed: float):
    FRmotor(False, speed)
    FLmotor(False, speed)
    BRmotor(False, speed)
    BLmotor(False, speed)

def moveLeft(speed: float):
    FRmotor(True, speed)
    FLmotor(False, speed)
    BRmotor(False, speed)
    BLmotor(True, speed)

def moveRight(speed: float):
    FRmotor(False, speed)
    FLmotor(True, speed)
    BRmotor(True, speed)
    BLmotor(False, speed)
    
def turnLeft(speed: float):
    FRmotor(True, speed)
    FLmotor(False, speed)
    BRmotor(True, speed)
    BLmotor(False, speed)

def turnRight(speed: float):
    FRmotor(False, speed)
    FLmotor(True, speed)
    BRmotor(False, speed)
    BLmotor(True, speed)
    
    
    
    
#Pygame Loop
while True:
    
    events = pygame.event.get()
    
    for event in events:
        
        #If/While key is pressed
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                #Update display
                pygame.draw.circle(screen, (0,255,0), (0,0), 100)
                pygame.display.update()
                
                #Move Motors
                moveForward(0.7)
                
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                #Update display
                pygame.draw.circle(screen, (0,255,0), (800,0), 100)
                pygame.display.update()
                
                #Move Motors
                moveLeft(0.7)
                
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                #Update display
                pygame.draw.circle(screen, (0,255,0), (800,400), 100)
                pygame.display.update()
                
                #Move Motors
                moveBackward(0.7)
                
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                #Update display
                pygame.draw.circle(screen, (0,255,0), (0,400), 100)
                pygame.display.update()
                
                #Move Motors
                moveRight(0.7)
                
                
        #When key is released 
        if event.type == pygame.KEYUP:
            
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                #Update display
                pygame.draw.circle(screen, (255,0,0), (0,0), 100)
                pygame.display.update()
                
                #Stop motors
                StopMotors()
                
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                #Update display
                pygame.draw.circle(screen, (255,0,0), (800,0), 100)
                pygame.display.update()
                
                #Stop motors
                StopMotors()
                
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                #Update display
                pygame.draw.circle(screen, (255,0,0), (800,400), 100)
                pygame.display.update()
                
                #Stop motors
                StopMotors()
                
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                #Update display
                pygame.draw.circle(screen, (255,0,0), (0,400), 100)
                pygame.display.update()
                
                #Stop motors
                StopMotors()