# coding:utf-8
# pylint: disable=no-member
# pylint: disable=pointless-string-statement
# pylint: disable=missing-docstring


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

    def __init__(self, file):
        self.file = file
        self.structure = []

    def generate(self):

        """generation from the map files of a structure
         of characters associated with the sprites"""

        with open(self.file + ".txt") as var_file:
            structure_level = []
            # Browse the lines of the file
            for line in var_file:
                line_level = []
                # Browse the sprites (letters) in the file
                for sprite in line:
                    # ignore \n at the end of line
                    if sprite != '\n':
                        # add sprite to the list of line
                        line_level.append(sprite)
                # add line to the list of the level
                structure_level.append(line_level)
            # record
            self.structure = structure_level
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
                x_value = num_case * cons.SPRITE_SIZE_PIXEL
                y_value = num_line * cons.SPRITE_SIZE_PIXEL
                if sprite == 'm':  # m = wall
                    screen.blit(wall, (x_value, y_value))
                elif sprite == 'd':  # d = start
                    screen.blit(start, (x_value, y_value))
                elif sprite == 'a':  # a = arrival
                    screen.blit(arrival, (x_value, y_value))
                elif sprite == 'g':  # g = guardian
                    screen.blit(guardian, (x_value, y_value))
                elif sprite == 'l':  # l = needle
                    screen.blit(needle, (x_value, y_value))
                elif sprite == 't':  # t = tube
                    screen.blit(tube, (x_value, y_value))
                elif sprite == 's':  # s = exit
                    screen.blit(syringe, (x_value, y_value))
                num_case += 1
            num_line += 1


class Player:
    """class creating player"""

    def __init__(self, image, level):
        # Sprites of the player
        self.image_player = pygame.image.load(image).convert_alpha()
        # Position of the player in cases and pixels
        self.case_x = 0
        self.case_y = 0
        self.x_value = 0
        self.y_value = 0
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
                if self.level.structure[self.case_y][self.case_x + 1] != 'm':
                    # moving one case
                    self.case_x += 1
                    # pixel position
                    self.x_value = self.case_x * cons.SPRITE_SIZE_PIXEL

        # LEFT
        if direction == 'left':
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x - 1] != 'm':
                    self.case_x -= 1
                    self.x_value = self.case_x * cons.SPRITE_SIZE_PIXEL

        # UP
        if direction == 'up':
            if self.case_y > 0:
                if self.level.structure[self.case_y - 1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y_value = self.case_y * cons.SPRITE_SIZE_PIXEL

        # DOWN
        if direction == 'down':
            if self.case_y < (cons.MAX_SPRITES_SIZE - 1):
                if self.level.structure[self.case_y + 1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y_value = self.case_y * cons.SPRITE_SIZE_PIXEL

        # if objects at the case recovery in bag
        if self.level.structure[self.case_y][self.case_x] in cons.OBJECTS_SPRITES:
            # add into the bag
            self.bag.append(self.level.structure[self.case_y][self.case_x])
            # del objet of the map
            self.level.structure[self.case_y][self.case_x] = ""


class Button:
    """ objects buttons are surface clickable or not  """

    def __init__(self, text, color, FONT_SIZE, emplacement, picture,
                 picture_press, blank_color=None):
        """ Button with attributes: text, emplacement, pict, pict when the button is pressed"""

        font = pygame.font.SysFont("arial", FONT_SIZE, cons.BOLD, cons.ITALIC)
        self.text = text
        self.color = color
        self.font_size = FONT_SIZE
        self.text_surf = font.render(self.text, True, self.color)
        self.text_rect = self.text_surf.get_rect()
        self.emplacement = emplacement
        self.picture = picture
        self.picture_press = picture_press
        self.image = pygame.image.load(self.picture_press).convert()
        self.image_rect = self.image.get_rect().move(emplacement)
        self.position_text = ()
        self.blank_color = blank_color
        # Center the text into the button
        xi_value, yi_value = self.image_rect.x, self.image_rect.y
        width, height = self.image_rect.w, self.image_rect.height
        w_value, h_value = self.text_rect.w, self.text_rect.h
        # final coordinates of the text rect
        self.xf_value = xi_value + (width / 2) - (w_value / 2)
        self.yf_value = yi_value + (height / 2) - (h_value / 2)
        self.position_text = self.xf_value, self.yf_value

    def stick(self, surface, press=None):
        """ blit the button to the surface, pressed or not """

        font = pygame.font.SysFont("arial", self.font_size, cons.BOLD, cons.ITALIC)

        # if the button is pressed
        if press == "press":
            self.image = pygame.image.load(self.picture_press).convert()
            self.image.set_colorkey(self.blank_color)
            self.image_rect = self.image.get_rect().move(self.emplacement)
            surface.blit(self.image, self.image_rect)
            if len(self.text.splitlines()) != 1:  # If the text got multiple lines
                xf_value, yf_value = self.image_rect.topleft
                for line in self.text.splitlines():
                    print(xf_value, yf_value)
                    surface.blit(font.render(line, True, self.color), (xf_value, yf_value))
                    yf_value += self.font_size
            else:
                surface.blit(self.text_surf, self.position_text)  # If text is just one word
        else:
            self.image = pygame.image.load(self.picture).convert()
            self.image.set_colorkey(self.blank_color)
            self.image_rect = self.image.get_rect().move(self.emplacement)
            surface.blit(self.image, self.image_rect)
            if len(self.text.splitlines()) != 1:
                xf_value, yf_value = self.image_rect.topleft
                for line in self.text.splitlines():
                    surface.blit(font.render(line, True, self.color), (xf_value, yf_value))
                    yf_value += self.font_size
            else:
                surface.blit(self.text_surf, self.position_text)
