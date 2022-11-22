import pygame


class GameLoop:
    def __init__(self, level, renderer, clock):
        self._level = level
        self._renderer = renderer
        self._clock = clock

    def start(self):
        while True:
            if self._handle_events() == False:
                break
            self._level.move_car()
            current_time = self._clock.get_ticks()

            self._render()

            self._clock.tick(60)

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self._level.add_speed("left")
                if event.key == pygame.K_RIGHT:
                    self._level.add_speed("right")
            elif event.type == pygame.QUIT:
                return False

    def _render(self):
        self._renderer.render()