import pygame
from circleshape import CircleShape
from constants import *
import random

class DoubleXPItem(CircleShape):
    def __init__(self):
        x = random.randint(50, SCREEN_WIDTH-50)
        y = random.randint(50, SCREEN_HEIGHT-50)
        super().__init__(x, y, SHOT_RADIUS*2)

    def draw(self, screen):
        pygame.draw.circle(screen, "green", (int(self.position.x), int(self.position.y)), self.radius, 2)

    def update(self, dt):
        pass #no movement 