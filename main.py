import pygame
import sys
from pendulum import Pendulum


SCREEN_SIZE = [1000, 800]


def main() -> None:

    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("Double Pendulum simultor")
    clock = pygame.time.Clock()
    pendulum = Pendulum()

    x_offset = screen.get_width()/2
    y_offset = screen.get_height()/4

    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pendulum.update()
        pygame.draw.rect(surface = screen, color = (0, 0, 0), rect = (0, 0, screen.get_width(), screen.get_height()))
        pendulum.render(screen, (x_offset, y_offset))
        clock.tick(60)
        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == '__main__':
    main()