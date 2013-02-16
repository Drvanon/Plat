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
        self.surf = "" # TODO Make this actable
        self.rect = ""

    def render(self, campos, background, width, height):
        background.blit(self.surf, 
                (width / 2 + (self.rect.width * 10) - campos[0],
                    height / 2 + self.rect.height * 10 - campos[1]))

class Scene(object):
    def __init__(self):
        self.texts = []
        self.background_image = None

    def render(self, background):
        background.blit(self.background_image, (0, 0))
        for text in self.texts:
            background.blit(*text.getrender())

class Level(Scene):
    def __init__(self, screen, background):
        self.blocks = []
        self.camera = Camera(self, screen, background)

    def render(self):
        for block in self.blocks:
            block.render()

class Camera(object):
    def __init__(self, level, screen, background):
        self.level = level
        self.position = [0, 0]
        self.screen = screen
        self.background = background

    def render(self):
        width = window.get_width()
        height = window.get_height()
        for block in level.blocks:
            # Is block within camera range?
            if  block.position[0] < self.pos[0] + width  / 2 and \
                block.position[0] > self.pos[0] - width  / 2 and \
                block.position[1] < self.pos[1] + height / 2 and \
                blocl.position[1] > self.pos[1] - height / 2:
                    block.render(self.pos, self.background, width, height)
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
