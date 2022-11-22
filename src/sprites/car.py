import pygame
from load_image import load_image


class Car(pygame.sprite.Sprite):
    def __init__(self, x=600, y=600):
        super().__init__()

        self.image = load_image("car.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 0
        self.max_speed = 10

