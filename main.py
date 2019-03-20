# coding:utf-8
# pylint: disable=invalid-name
# pylint: disable=no-member
# pylint: disable=missing-docstring

# Third party imports
import pygame

# Local application imports
from modules.classes import Level, Player
import modules.buttons as but
import modules.constants as cons


"""
Main file

"""

# Screen
# The video mode is in the buttons.py file
home = pygame.image.load(cons.IMAGE_HOME).convert()  # Back screen home image
pygame.display.set_caption(cons.TITLE_SCREEN)  # Window title
surf_player = pygame.image.load(cons.IMAGE_PLAYER).convert_alpha()
pygame.display.set_icon(surf_player)  # Window icon

# MAIN LOOP
launched_main = 1
while launched_main:
    launched_main_game = 1
    launched_main_home = 1
    level_launched = 1
    # BOUCLE D'home
    while launched_main_home:
        # Speed limitation and mouse position
        pygame.time.Clock().tick(100)
        mouse = pygame.mouse.get_pos()
        but.SCR.blit(home, (0, 0))
        but.B_TITLE.stick(but.SCR)
        but.B_RULES.stick(but.SCR)
        but.B1.stick(but.SCR)  # non pressed button
        but.B2.stick(but.SCR)
        # PLAY
        if but.B1.image_rect.collidepoint(mouse):
            but.B1.stick(but.SCR, "press")
        # QUIT
        if but.B2.image_rect.collidepoint(mouse):
            but.B2.stick(but.SCR, "press")
        # RULES
        if but.B_RULES.image_rect.collidepoint(mouse):
            but.B_RULES2.stick(but.SCR)
        for event in pygame.event.get():
            # Exit conditions
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN \
                    and event.key == pygame.K_ESCAPE:
                launched_main_home = 0
                level_launched = 0
                launched_main_game = 0
                launched_main = 0
            # MOUSE LEFT CLICK UP
            choice = 0
            # If button UP
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if but.B1.image_rect.collidepoint(mouse):
                    but.B1.stick(but.SCR, "press")
                    launched_main_home = 0
                    choice = 'resources/maps/n1'
                if but.B2.image_rect.collidepoint(mouse):
                    but.B2.stick(but.SCR, "press")
                    launched_main_home = 0
                    launched_main_game = 0
                    launched_main = 0
        pygame.display.flip()

    # Loading background
    fond = pygame.image.load(cons.IMAGE_FOND).convert()
    fond.fill(cons.BLACK)
    # Level generation
    level = Level(choice)
    level.generate()
    level.display(but.SCR)
    # player generation
    mac_giver = Player(cons.IMAGE_PLAYER, level)

    # GAME LOOP
    win_lose = False
    while launched_main_game:
        # Loop speed limitation
        pygame.time.Clock().tick(30)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                launched_main_game = 0
                launched_main = 0
            elif event.type == pygame.KEYDOWN:
                # if escape come back to menu
                if event.key == pygame.K_ESCAPE:
                    launched_main_game = 0
                # movement of mac gyver
                elif event.key == pygame.K_RIGHT and win_lose is False:
                    mac_giver.move('right')
                elif event.key == pygame.K_LEFT and win_lose is False:
                    mac_giver.move('left')
                elif event.key == pygame.K_UP and win_lose is False:
                    mac_giver.move('up')
                elif event.key == pygame.K_DOWN and win_lose is False:
                    mac_giver.move('down')
            # display character at new position
            but.SCR.blit(fond, (0, 0))
            level.display(but.SCR)
            but.SCR.blit(mac_giver.image_player, (mac_giver.x_value, mac_giver.y_value))
            pygame.display.flip()
            # End
            # Win
            if level.structure[mac_giver.case_y][mac_giver.case_x] == 'a':
                win_lose = True
                but.B_WIN.stick(but.SCR)
                but.B_MENU.stick(but.SCR)
                but.B2.stick(but.SCR)
            # Lose
            if level.structure[mac_giver.case_y][mac_giver.case_x] == 'g' and \
                    len(mac_giver.bag) != 3:
                win_lose = True
                but.B_LOSE.stick(but.SCR)
                but.B_MENU.stick(but.SCR)
                but.B2.stick(but.SCR)
            # MENU
            # win_lose true if game is finished
            if but.B_MENU.image_rect.collidepoint(mouse) and win_lose:
                but.B_MENU.stick(but.SCR, "press")
            # QUIT
            if but.B2.image_rect.collidepoint(mouse) and win_lose:
                but.B2.stick(but.SCR, "press")
            # MOUSE LEFT CLICK UP
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and \
                    win_lose:  # If button UP
                if but.B_MENU.image_rect.collidepoint(mouse):
                    but.B_MENU.stick(but.SCR, "press")
                    launched_main_game = 0
                if but.B2.image_rect.collidepoint(mouse):
                    but.B2.stick(but.SCR, "press")
                    launched_main_home = 0
                    launched_main_game = 0
                    launched_main = 0
            # if length of bag == 0
            if len(mac_giver.bag) == 0:
                but.B_SCORE0.stick(but.SCR)
            elif len(mac_giver.bag) == 1:
                but.B_SCORE1.stick(but.SCR)
            elif len(mac_giver.bag) == 2:
                but.B_SCORE2.stick(but.SCR)
            elif len(mac_giver.bag) == 3:
                but.B_SCORE3.stick(but.SCR)

            pygame.display.flip()
