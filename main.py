import pygame, sys, time

TBF = 1 # Time Between Frames (in seconds)

pygame.init()

stdFont = pygame.font.Font(None, 30)

class Text(object):
    def __init__(self, string, color, position):
        self.string = string
        self.color = color
        self.position = position

    def getrender(self):
        surf = stdFont.render(self.string, 1, self.color)
        rect = surf.get_rect()
        rect.center = self.position
        return surf, rect

class Block(pygame.sprite):
    def __init__(self):
        self.blockpos = []
        self.blockimage = ""

class Scene(object):
    def __init__(self):
        self.texts = []
        self.background_image = None

    def render(self, background):
        background.blit(self.background_image, (0, 0))
        for text in self.texts:
            background.blit(*text.getrender())

class Level(Scene):
    def __init__(self):
        self.blocks = []

    def render(self):
        for block in self.blocks:
            block.render()

class Camera():
    def __init__(self, level, screen):
        self.level = level
        self.position = [0, 0]
        self.screen = screen

def __main__():
    screen = pygame.display.set_mode([500, 500])

    start = time.time()

    opening_scene = Scene()
    welcome_text = Text('Welcome to Plat', (240, 10, 240), (screen.get_size()[0] /2, screen.get_size()[1] /2))
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
