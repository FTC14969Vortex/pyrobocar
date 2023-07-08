from pyfirmata import ArduinoMega
import pygame

#Set up board port
board = ArduinoMega("/dev/cu.usbmodem14101")

#Init pygame and pygame screen
pygame.init
screen = pygame.display.set_mode((1000,500), pygame.RESIZABLE)
pygame.display.set_caption("Robot Controller")

#Set up the black color
BLACK = (0,0,0)
BLUE = (2,130,242)

#Set up the run variable for the main WHILE loop. When run is false the game will stop.
Run = True


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
    
    
    
    


#Position for the circle/robot to draw
x = 400
y = 200

#Pygame Loop
while Run:
    
    #Reset the screen
    screen.fill(BLACK)
    
    #Draw the circle
    pygame.draw.circle(screen, BLUE, (x,y), 25)
    
    keys = pygame.key.get_pressed()
    
    #Moves circle and motor based off keypress
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        y -= 5
        moveForward(2)
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        y += 5
        moveBackward(2)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        x += 5
        moveRight(2)
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        x -= 5
        moveLeft(2)
    
    #Stop the motors and update the display
    StopMotors()
    pygame.display.update()
    
    
    #Quits the game
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Run = False
        if event.type == pygame.QUIT:
            Run = False
                
pygame.quit