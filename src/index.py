import pygame
from clock import Clock
from renderer import Renderer
from game_loop import GameLoop
from level import Level

def main():
    display = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("TURBO MAX SPEED RACER!")
    level = Level()
    renderer = Renderer(display, level)
    clock = Clock()
    game_loop = GameLoop(level, renderer, clock)
    game_loop.start()

if __name__ == "__main__":
    main()