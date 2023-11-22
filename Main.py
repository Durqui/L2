import pygame
from pygame import K_ESCAPE
import random
import time

# Variables to create colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orng = (255, 80, 0)
blue = (0, 0, 255)
Lblue = (0, 110, 255)
green = (0, 255, 0)

# sets frame rate
fps = pygame.time.Clock

# Screen size
screen = pygame.display.set_mode((600, 400))

# Name of the window
pygame.display.set_caption('L2 Test window')

# Fills the screen with a color
screen.fill(black)

# Updates screen
pygame.display.flip()

# Makes the program run
running = True


# Base entity class
class Base(pygame.sprite.Sprite):
    def __init__(self, display, color, width, height, cords, radius):
        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.image.set_colorkey(color)

        self.display = display
        self.color = color
        self.width = width
        self.height = height
        self.local = cords
        self.radius = radius

    def draw(self):
        pygame.draw.circle(self.display, self.color, self.local, self.radius)


Earth = Base(screen, Lblue, 6, 7, (390, 150), 29)
Sun = Base(screen, orng, 6, 7, (300, 210), 50)

while running:
    # Constantly checks for event
    for event in pygame.event.get():
        # Makes escape close the window
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
    # Initiates pygame
    pygame.init()
    # Display update keeps updating the screens
    pygame.display.update()
    Earth.draw()
    Sun.draw()
