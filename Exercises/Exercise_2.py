from pyfirmata import ArduinoMega, SERVO, OUTPUT
import time
import pygame

board = ArduinoMega("/dev/cu.usbmodem14401")

servoPin = 13

board.digital[servoPin].mode = SERVO


#Init pygame and pygame screen
pygame.init
screen = pygame.display.set_mode((1000,500), pygame.RESIZABLE)
pygame.display.set_caption("Servo Control")

GREEN = (79,121,66)
BLUE = (2,130,242)

def rotateServo(angle):
    board.digital[servoPin].write(angle)

Run = True

x = 500
y = 250

while Run:
    
    keys = pygame.key.get_pressed()
    
    #Moves circle and motor based off keypress
    if keys[pygame.K_o]:
        rotateServo(0)
        pygame.draw.circle(screen, BLUE, (x,y), 25)


    if keys[pygame.K_c]:
        rotateServo(180)
        pygame.draw.circle(screen, GREEN, (x,y), 25)

    
    
    #Quits the game
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Run = False
        if event.type == pygame.QUIT:
            Run = False
                
pygame.quit