import pygame, sys, time, level

TBF = 1 # Time Between Frames (in seconds)

pygame.init()

stdFont = pygame.font.Font(None, 30)

def __main__():
    screen = pygame.display.set_mode([500, 500])

    start = time.time()

    opening_scene = level.Scene()
    welcome_text = level.Text('Welcome to Plat', (240, 10, 240), (screen.get_size()[0] /2, screen.get_size()[1] /2))
    opening_scene.texts.append(welcome_text)
    cur_scene = opening_scene

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

        cur_scene.render(background)
        screen.blit(background, (0, 0))
        pygame.display.flip()

if __name__ == "__main__": __main__()
