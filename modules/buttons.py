# coding:utf-8
# pylint: disable=missing-docstring

# Third party imports
import pygame

# Local application imports
from modules.classes import Button
import modules.constants as cons


""" file regrouping the button's instantiations
for simplification of the main file """


# screen video mode
SCR = pygame.display.set_mode(cons.SCR_SIZE)

# Buttons
# Menu Start
B1 = Button("PLAY",
            cons.FONT_COLOR,
            cons.FONT_SIZE,
            cons.POSITION_B1,
            cons.IMAGE_BUTTON,
            cons.IMAGE_BOUT_PRESS,
            cons.WHITE)
# Menu QUIT
B2 = Button("QUIT",
            cons.FONT_COLOR,
            cons.FONT_SIZE,
            cons.POSITION_B2,
            cons.IMAGE_BUTTON,
            cons.IMAGE_BOUT_PRESS,
            cons.WHITE)
# Menu Title
B_TITLE = Button("MacGyver",
                 cons.BLUE,
                 cons.FONT_SIZE,
                 cons.POSITION_B_TITLE,
                 cons.IMAGE_BUTTON,
                 cons.IMAGE_BUTTON,
                 cons.WHITE)
# Menu RULES
B_RULES = Button("RULES",
                 cons.FONT_COLOR,
                 cons.FS_RULES,
                 cons.POSITION_B_RULES,
                 cons.IMAGE_RULES,
                 cons.IMAGE_RULES,
                 cons.WHITE)
# Menu RULES text
B_RULES2 = Button(cons.RULES,
                  cons.BLACK,
                  20,
                  cons.POSITION_BR2,
                  cons.IMAGE_RULES2,
                  cons.IMAGE_RULES2,
                  cons.BLACK)
# Level title
B_LEVEL_TITLE = Button("Levels",
                       cons.BLUE,
                       cons.FONT_SIZE,
                       cons.POSITION_B_TITLE,
                       cons.IMAGE_BUTTON,
                       cons.IMAGE_BUTTON,
                       cons.WHITE)
# Level 1
B_LEVEL1 = Button(" > Level 1",
                  cons.FONT_COLOR,
                  30,
                  cons.POS_LEVEL1,
                  cons.IMAGE_BUTTON,
                  cons.IMAGE_BOUT_PRESS,
                  cons.WHITE)

# End Menu
B_MENU = Button("MENU",
                cons.FONT_COLOR,
                50,
                cons.POSITION_B1,
                cons.IMAGE_BUTTON,
                cons.IMAGE_BOUT_PRESS,
                cons.WHITE)
# End Win
B_WIN = Button("YOU WIN !",
               cons.GREEN,
               cons.FONT_SIZE,
               (150, 150),
               cons.IMAGE_BUTTON,
               cons.IMAGE_BUTTON,
               cons.WHITE)
# End Lose
B_LOSE = Button("YOU LOSE...",
                cons.RED,
                cons.FONT_SIZE,
                (150, 150),
                cons.IMAGE_BUTTON,
                cons.IMAGE_BUTTON,
                cons.WHITE)
