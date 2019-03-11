""" fichier regrouping the button's instantiations
for simplification of the main fichier """
# coding:utf-8
from modules.classes import *

# screen video mode
scr = pygame.display.set_mode(scrSize)

# Buttons --------------------------------------------------------------------
# Menu Start
b1 = Button("PLAY",
            fontColor,
            fontSize,
            position_b1,
            image_button,
            image_bout_press,
            white)
# Menu QUIT
b2 = Button("QUIT",
            fontColor,
            fontSize,
            position_b2,
            image_button,
            image_bout_press,
            white)
# Menu Title
b_title = Button("MacGyver",
                 blue,
                 fontSize,
                 position_b_title,
                 image_button,
                 image_button,
                 white)
# Menu Rules
b_rules = Button("Rules",
                 fontColor,
                 fsRules,
                 position_b_rules,
                 image_rules,
                 image_rules,
                 white)
# Menu rules text
b_rules2 = Button(rules,
                  black,
                  20,
                  position_br2,
                  image_rules2,
                  image_rules2,
                  black)
# Level title
b_level_title = Button("Levels",
                       blue,
                       fontSize,
                       position_b_title,
                       image_button,
                       image_button,
                       white)
# Level 1
b_level1 = Button(" > Level 1",
                  fontColor,
                  30,
                  pos_level1,
                  image_button,
                  image_bout_press,
                  white)
# Level 2
b_level2 = Button(" > Level 2",
                  fontColor,
                  30,
                  pos_level2,
                  image_button,
                  image_bout_press,
                  white)
# Level back
b_back = Button("Back",
                fontColor,
                20,
                pos_back,
                image_button,
                image_button,
                white)
# End Menu
b_menu = Button("MENU",
                fontColor,
                50,
                position_b1,
                image_button,
                image_bout_press,
                white)
# End Win
b_win = Button("YOU WIN !",
               green,
               fontSize,
               (150, 150),
               image_button,
               image_button,
               white)
# End Lose
b_lose = Button("YOU LOSE...",
                red,
                fontSize,
                (150, 150),
                image_button,
                image_button,
                white)

