# coding:utf-8
""" Main file """
from buttons import *

# Screen ---------------------------------------------------------------------
# The video mode is in the buttons.py file
accueil = pygame.image.load(image_accueil).convert()  # Back
pygame.display.set_caption(title_screen)  # Window title
surf_player = pygame.image.load(image_player).convert_alpha()
pygame.display.set_icon(surf_player)  # Window icon

# MAIN LOOP ------------------------------------------------------------------
continuer = 1
while continuer:
    # On remet ces variables à 1 à chaque tour de boucle
    continuer_jeu = 1
    continuer_accueil = 1
    level_launched = 1
    # BOUCLE D'ACCUEIL -------------------------------------------------------
    while continuer_accueil:
        # Speed limitation and mouse position
        pygame.time.Clock().tick(100)
        mouse = pygame.mouse.get_pos()
        scr.blit(accueil, (0, 0))
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
                continuer_accueil = 0
                level_launched = 0
                continuer_jeu = 0
                continuer = 0
            # MOUSE LEFT CLICK UP
            choix = 0
            # If button UP
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                if b1.imageRect.collidepoint(mouse):
                    b1.stick(scr, "press")
                    continuer_accueil = 0
                    choix = 'resources/maps/n1'
                if b2.imageRect.collidepoint(mouse):
                    b2.stick(scr, "press")
                    continuer_accueil = 0
                    continuer_jeu = 0
                    continuer = 0
        pygame.display.flip()
    # ------------------------------------------------------------------------
    # Features Levels
    # ------------------------------------------------------------------------
    # Loading background
    fond = pygame.image.load(image_fond).convert()
    fond.fill(black)
    # Level generation
    level = Level(choix)
    level.generate()
    level.display(scr)
    # player generation
    mac_giver = Player(image_player, level)
    # GAME LOOP --------------------------------------------------------------
    win_lose = False
    while continuer_jeu:
        # Loop speed limitation
        pygame.time.Clock().tick(30)
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer_jeu = 0
                continuer = 0
            elif event.type == pygame.KEYDOWN:
                # if escape come back to menu
                if event.key == pygame.K_ESCAPE:
                    continuer_jeu = 0
                # deplacement touch of mac gyver
                elif event.key == pygame.K_RIGHT and win_lose is False:
                    mac_giver.move('right')
                elif event.key == pygame.K_LEFT and win_lose is False:
                    mac_giver.move('left')
                elif event.key == pygame.K_UP and win_lose is False:
                    mac_giver.move('up')
                elif event.key == pygame.K_DOWN and win_lose is False:
                    mac_giver.move('down')
            # Affichages aux nouvelles positions
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
            # win_lose true if game finished
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
                    continuer_jeu = 0
                if b2.imageRect.collidepoint(mouse):
                    b2.stick(scr, "press")
                    continuer_accueil = 0
                    continuer_jeu = 0
                    continuer = 0

            pygame.display.flip()
