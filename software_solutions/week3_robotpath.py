import pygame
import math
from matplotlib import pyplot as plt


class PathLissajous:
    def __init__(self, xAmplitude, yAmplitude, xFrequency, yFrequency, delta):
        self.xAmp = xAmplitude
        self.yAmp = yAmplitude
        self.xFreq = xFrequency
        self.yFreq = yFrequency
        self.xyDelay = delta

    def generate_path(self, num_points):
        path = []
        for i in range(num_points):
            t = i * 2 * math.pi / num_points
            x = self.xAmp * math.sin(self.xFreq * t + self.xyDelay)
            y = self.yAmp * math.sin(self.yFreq * t)
            path.append((x, y))
        return path

    def plot_path(self, num_points):
        path = self.generate_path(num_points)
        x, y = zip(*path)
        plt.plot(x, y)
        plt.show()


class MecanumChassis:
    def __init__(self, x, y):
        self.x = x  # Current location of the car.
        self.y = y  # Current location of the car.
        self.speed = 50  # You can adjust the speed as needed
        self.directions = {
            "forward": (0, -1),
            "backward": (0, 1),
            "left": (-1, 0),
            "right": (1, 0),
        }

    def display(self, screen, sprite):
        screen.blit(sprite, (self.x, self.y))

    def move(self, direction, distance):
        dx, dy = self.directions[direction]
        self.x += dx * distance * self.speed
        self.y += dy * distance * self.speed

    def drive_forward(self, distance):
        self.move("forward", distance)

    def drive_backward(self, distance):
        self.move("backward", distance)

    def turn_right(self, distance):
        self.move("right", distance)

    def turn_left(self, distance):
        self.move("left", distance)

    def strafe_right(self, distance):
        self.move("right", distance)

    def strafe_left(self, distance):
        self.move("left", distance)


def main():
    ## Create a Liassajous path and plot it.
    lissajous = PathLissajous(...)
    lissajous.plot_path(750)

    # # Create a Liassajous path and move the car along it.

    # pygame.init()
    # screen = pygame.display.set_mode((800, 600))
    # sprite = pygame.image.load(
    #     "/Users/mehtas/Documents/GitHub/pyrobocar/software_solutions/square.png"
    # )
    # sprite = pygame.transform.scale(sprite, (30, 30))
    # mecanum_chassis = MecanumChassis(400, 300)

    # lissajous = PathLissajous(
    #     200, 200, 5, 10, -math.pi / 2
    # )  # These are example parameters
    # path = lissajous.generate_path(750)  # Generate the Lissajous path

    # running = True
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False

    #     screen.fill((0, 0, 0))
    #     for x, y in path:
    #         mecanum_chassis.x = (
    #             400 + x
    #         )  # Update the chassis position based on the Lissajous path
    #         mecanum_chassis.y = 300 + y
    #         mecanum_chassis.display(screen, sprite)
    #         pygame.display.flip()
    #         pygame.time.wait(
    #             2
    #         )  # Wait for a short time to control the speed of the animation


if __name__ == "__main__":
    main()
