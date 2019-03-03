# coding:utf-8
""" Main fichier """
from buttons import *

# Screen ---------------------------------------------------------------------
# The video mode is in the buttons.py fichier
home = pygame.image.load(image_home).convert()  # Back screen home image
pygame.display.set_caption(title_screen)  # Window title
surf_player = pygame.image.load(image_player).convert_alpha()
pygame.display.set_icon(surf_player)  # Window icon

# MAIN LOOP ------------------------------------------------------------------
launched_main = 1
while launched_main:
    launched_main_game = 1
    launched_main_home = 1
    level_launched = 1
    # BOUCLE D'home -------------------------------------------------------
    while launched_main_home:
        # Speed limitation and mouse position
        pygame.time.Clock().tick(100)
        mouse = pygame.mouse.get_pos()
        scr.blit(home, (0, 0))
        b_title.stick(scr)
        b_rules.stick(scr)
        b1.stick(scr)  # non pressed button
        b2.stick(scr)
        # PLAY
        if b1.imageRect.collidepoint(mouse):
            b1.stick(scr, "press")
        # QUIT
        if b2.imageRect.collidepoint(mouse):
            b2.stick(scr, "press")
        # RULES
        if b_rules.imageRect.collidepoint(mouse):
            b_rules2.stick(scr)
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
                if b1.imageRect.collidepoint(mouse):
                    b1.stick(scr, "press")
                    launched_main_home = 0
                    choice = 'resources/maps/n1'
                if b2.imageRect.collidepoint(mouse):
                    b2.stick(scr, "press")
                    launched_main_home = 0
                    launched_main_game = 0
                    launched_main = 0
        pygame.display.flip()
    # ------------------------------------------------------------------------
    # Features Levels
    # ------------------------------------------------------------------------
    # Loading background
    fond = pygame.image.load(image_fond).convert()
    fond.fill(black)
    # Level generation
    level = Level(choice)
    level.generate()
    level.display(scr)
    # player generation
    mac_giver = Player(image_player, level)
    # GAME LOOP --------------------------------------------------------------
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
            scr.blit(fond, (0, 0))
            level.display(scr)
            scr.blit(mac_giver.image_player, (mac_giver.x, mac_giver.y))
            pygame.display.flip()
            # End-------------------------------------------------------------
            # Win
            if level.structure[mac_giver.case_y][mac_giver.case_x] == 'a':
                win_lose = True
                b_win.stick(scr)
                b_menu.stick(scr)
                b2.stick(scr)
            # Lose
            if level.structure[mac_giver.case_y][mac_giver.case_x] == 'g' and \
                    len(mac_giver.bag) != 3:
                win_lose = True
                b_lose.stick(scr)
                b_menu.stick(scr)
                b2.stick(scr)
            # MENU
            # win_lose true if game is finished
            if b_menu.imageRect.collidepoint(mouse) and win_lose:
                b_menu.stick(scr, "press")
            # QUIT
            if b2.imageRect.collidepoint(mouse) and win_lose:
                b2.stick(scr, "press")
            # MOUSE LEFT CLICK UP
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and \
                    win_lose:  # If button UP
                if b_menu.imageRect.collidepoint(mouse):
                    b_menu.stick(scr, "press")
                    launched_main_game = 0
                if b2.imageRect.collidepoint(mouse):
                    b2.stick(scr, "press")
                    launched_main_home = 0
                    launched_main_game = 0
                    launched_main = 0

            pygame.display.flip()
