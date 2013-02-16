import pygame, sys, time

TBF = 1 # Time Between Frames (in seconds)

pygame.init()

def __main__():
    screen = pygame.display.set_mode([500, 500])

    start = time.time()

    while 1:
        background = pygame.Surface(screen.get_size())
        background.convert()
        background.fill((0, 0, 0))

        sec = False
        if time.time() - start > TBF:
            sec = True
            start = time.time()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == "__main__": __main__()
