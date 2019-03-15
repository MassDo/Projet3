# coding:utf-8

# Standard library imports
import random

# Third party imports
import pygame

# Local application imports
import modules.constants as cons


""" 
Classes of the game Mc giver 

"""


pygame.init()


class Level:

    """class for the creation of a level"""

    def __init__(self, fichier):
        self.fichier = fichier
        self.structure = []

    def generate(self):

        """generation from the map fichier of a structure of characters associated with the sprites"""

        with open(self.fichier + ".txt") as var_fichier:
            structure_niveau = []
            # Browse the lines of the file
            for line in var_fichier:
                line_niveau = []
                # Browse the sprites (letters) in the fichier
                for sprite in line:
                    # ignore \n at the end of line
                    if sprite != '\n':
                        # add sprite to the list of line
                        line_niveau.append(sprite)
                # add line to the list of the level
                structure_niveau.append(line_niveau)
            # record
            self.structure = structure_niveau
            # add randomly the objects
            k = 0
            while k < 3:
                line = random.randrange(cons.MAX_SPRITES_SIZE)
                column = random.randrange(cons.MAX_SPRITES_SIZE)
                if self.structure[line][column] == "c":
                    self.structure[line][column] = cons.OBJECTS_SPRITES[k]
                    k += 1

    def display(self, screen):

        """ display of the level from structure and sprites"""

        wall = pygame.image.load(cons.IMAGE_WALL).convert()
        start = pygame.image.load(cons.IMAGE_START).convert()
        arrival = pygame.image.load(cons.IMAGE_ARRIVAL).convert_alpha()
        guardian = pygame.image.load(cons.IMAGE_GUARDIAN).convert_alpha()
        needle = pygame.image.load(cons.IMAGE_NEEDLE).convert_alpha()
        tube = pygame.image.load(cons.IMAGE_TUBE).convert_alpha()
        syringe = pygame.image.load(cons.IMAGE_SYRINGE).convert_alpha()

        # browse the list of the level
        num_line = 0
        for line in self.structure:
            # browse list of lines
            num_case = 0
            for sprite in line:
                # real position in pixels
                x = num_case * cons.SPRITE_SIZE_PIXEL
                y = num_line * cons.SPRITE_SIZE_PIXEL
                if sprite == 'm':		   # m = wall
                    screen.blit(wall, (x, y))
                elif sprite == 'd':		   # d = start
                    screen.blit(start, (x, y))
                elif sprite == 'a':		   # a = arrival
                    screen.blit(arrival, (x, y))
                elif sprite == 'g':		   # g = guardian
                    screen.blit(guardian, (x, y))
                elif sprite == 'l':		   # l = needle
                    screen.blit(needle, (x, y))
                elif sprite == 't':		   # t = tube
                    screen.blit(tube, (x, y))
                elif sprite == 's':		   # s = exit
                    screen.blit(syringe, (x, y))
                num_case += 1
            num_line += 1


class Player:

    """class creating player"""

    def __init__(self, image, level):
        # Sprites of the player
        self.IMAGE_PLAYER = pygame.image.load(image).convert_alpha()
        # Position of the player in cases and pixels
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        # level where the player is
        self.level = level
        # bag of the player
        self.bag = []

    def move(self, direction):

        """ moving player """

        # RIGHT
        if direction == 'right':
            # checking we are staying into the screen
            if self.case_x < (cons.MAX_SPRITES_SIZE - 1):
                # checking destination case not a wall
                if self.level.structure[self.case_y][self.case_x+1] != 'm':
                    # moving one case
                    self.case_x += 1
                    # pixel position
                    self.x = self.case_x * cons.SPRITE_SIZE_PIXEL

        # LEFT
        if direction == 'left':
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x-1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x * cons.SPRITE_SIZE_PIXEL

        # UP
        if direction == 'up':
            if self.case_y > 0:
                if self.level.structure[self.case_y-1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y = self.case_y * cons.SPRITE_SIZE_PIXEL

        # DOWN
        if direction == 'down':
            if self.case_y < (cons.MAX_SPRITES_SIZE - 1):
                if self.level.structure[self.case_y+1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y = self.case_y * cons.SPRITE_SIZE_PIXEL

        # if objects at the case recovery in bag
        if self.level.structure[self.case_y][self.case_x] in cons.OBJECTS_SPRITES:
            # add into the bag
            self.bag.append(self.level.structure[self.case_y][self.case_x])
            # del objet of the map
            self.level.structure[self.case_y][self.case_x] = ""


class Button:

    """ objects buttons are surface clickable or not  """

    def __init__(self, text, color, FONT_SIZE, emplacement, picture, picture_press, blank_color=None):
        """ Button with attributes: text, emplacement, pict, pict when the button is pressed"""

        font = pygame.font.SysFont("arial", FONT_SIZE, cons.BOLD, cons.ITALIC)
        self.text = text
        self.color = color
        self.font_size = FONT_SIZE
        self.textSurf = font.render(self.text, True, self.color)
        self.textRect = self.textSurf.get_rect()
        self.emplacement = emplacement
        self.picture = picture
        self.picturePress = picture_press
        self.image = pygame.image.load(self.picturePress).convert()
        self.imageRect = self.image.get_rect().move(emplacement)
        self.positionText = ()
        self.blank_color = blank_color
        # Center the text into the button
        xi, yi, width, height = self.imageRect.x, self.imageRect.y, self.imageRect.w, self.imageRect.height
        w, h = self.textRect.w, self.textRect.h
        # final coordinates of the text rect
        self.xf = xi + (width/2) - (w/2)
        self.yf = yi + (height/2) - (h/2)
        self.positionText = self.xf, self.yf

    def stick(self, surface, press=None):
        """ blit the button to the surface, pressed or not """

        font = pygame.font.SysFont("arial", self.font_size, cons.BOLD, cons.ITALIC)

        # if the button is pressed
        if press == "press":
            self.image = pygame.image.load(self.picturePress).convert()
            self.image.set_colorkey(self.blank_color)
            self.imageRect = self.image.get_rect().move(self.emplacement)
            surface.blit(self.image, self.imageRect)
            if len(self.text.splitlines()) != 1:  # If the text got multiple lines
                xf, yf = self.imageRect.topleft
                for line in self.text.splitlines():
                    print(xf, yf)
                    surface.blit(font.render(line, True, self.color), (xf, yf))
                    yf += self.font_size
            else:
                surface.blit(self.textSurf, self.positionText)  # If text is just one word
        else:
            self.image = pygame.image.load(self.picture).convert()
            self.image.set_colorkey(self.blank_color)
            self.imageRect = self.image.get_rect().move(self.emplacement)
            surface.blit(self.image, self.imageRect)
            if len(self.text.splitlines()) != 1:
                xf, yf = self.imageRect.topleft
                for line in self.text.splitlines():
                    surface.blit(font.render(line, True, self.color), (xf, yf))
                    yf += self.font_size
            else:
                surface.blit(self.textSurf, self.positionText)
