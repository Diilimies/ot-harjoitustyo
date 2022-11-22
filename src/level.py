import pygame
from sprites.car import Car


class Level:
    def __init__(self) -> None:
        self.car = Car()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.car)
    
    def add_speed(self, direction):
        if direction == "right" and self.car.speed < self.car.max_speed:
            self.car.speed += 1
        if direction == "left" and self.car.speed > -self.car.max_speed:
            self.car.speed -= 1
    
    def move_car(self):
        self.car.rect.move_ip(self.car.speed, 0)