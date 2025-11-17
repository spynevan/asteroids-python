from circleshape import CircleShape
from constants import *
import pygame
import random
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,LINE_WIDTH)

    def update(self, delta_time):
        self.position += self.velocity * delta_time

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        new_asteroid_size = self.radius - ASTEROID_MIN_RADIUS
        log_event("asteroid_split")
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_asteroid_size)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_asteroid_size)

        theta = random.uniform(20,50)
        
        asteroid_1.velocity = self.velocity.rotate(theta) * 1.2 
        asteroid_2.velocity = self.velocity.rotate(- theta) * 1.2 

