from __future__ import print_function

import pygame, sys, yaml
import level

class OwnSpriteSheet(object):
    def __init__(self, filename, number_of_sprites, spritewidth=10, spriteheight=10):
        try:
            self.images = []
            self.sheet = pygame.image.load(filename)
            self.sheet_width = self.sheet.get_width()
            self.sheet_height = self.sheet.get_height()

            for i in range(number_of_sprites):
                x = i * spritewidth
                y = 0
                while x > self.sheet_width:
                    x -= self.sheet_width
                    y += spriteheight

                print(x, y)
                self.images.append(self.image_at((x, y, spritewidth, spriteheight)))

        except pygame.error:
            print("Unable to load spritesheet image:", filename)
            sys.exit(1)

    def image_at(self, rectangle, colorkey = None):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)

        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)

        return image

def spriteReader(filename):
    stream = open(filename, 'r')
    data = yaml.load_all(stream)

    blocks = []
    spritesheet = ""
    for dataset in data:
        if not "meta" in dataset:
            blocks.append(dataset)
        else:
            spritesheet = OwnSpriteSheet(dataset['sheetname'], dataset['nmbrofsprites'])

    all_blocks = {}
    for block in blocks:
        all_blocks[block['name']] = level.Block(
                block['name'],
                spritesheet.images[int(block['spritenmbr']) -1])
    return all_blocks

def test():
    pygame.init()

    screen = pygame.display.set_mode([500, 500])

    blocks = spriteReader('example.yaml')

    i = 0
    for block in blocks:
        pygame.image.save(blocks[block].image, 'test' + str(i) + ".png")
        i +=1

    while 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        pygame.display.flip()


if __name__ == "__main__": test()
