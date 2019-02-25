# coding:utf-8
from classes import *

# Initialisation ------------------------------------------------------------------------------------------------------
pygame.init()

# Screen --------------------------------------------------------------------------------------------------------------
scr = pygame.display.set_mode(scrSize)							# Window
accueil = pygame.image.load(image_accueil).convert()			# Back
pygame.display.set_caption(title_screen)						# Window title
surf_player = pygame.image.load(image_player).convert_alpha()
pygame.display.set_icon(surf_player)							# Window icon

# Buttons -------------------------------------------------------------------------------------------------------------
b1 = Button("PLAY", fontColor, fontSize, position_b1, image_boutton, image_bout_press, white)			# Menu Start
b2 = Button("QUIT", fontColor, fontSize, position_b2, image_boutton, image_bout_press, white)			# Menu QUIT
b_title = Button("MacGyver", blue, fontSize, position_b_title, image_boutton, image_boutton, white)	# Menu Title
b_rules = Button("Rules", fontColor, fsRules, position_b_rules, image_rules, image_rules, white)		# Menu Rules
b_rules2 = Button(rules, black, 20, position_br2, image_rules2, image_rules2, black)					# Menu rules text
b_level_title = Button("Levels", blue, fontSize, position_b_title, image_boutton, image_boutton, white)# Level title
b_level1 = Button(" > Level 1", fontColor, 30, pos_level1, image_boutton, image_bout_press, white)		# Level 1
b_level2 = Button(" > Level 2", fontColor, 30, pos_level2, image_boutton, image_bout_press, white)		# Level 2
b_back = Button("Back", fontColor, 20, pos_back, image_boutton, image_boutton, white)				# Level back
b_menu = Button("MENU", fontColor, fontSize, position_b1, image_boutton, image_bout_press, white)		# End Menu
b_win = Button("YOU WIN !", blue, fontSize, position_b_title, image_boutton, image_boutton, white)		# End Win
b_lose = Button("YOU LOSE...", blue, fontSize, position_b_title, image_boutton, image_boutton, white)	# End Lose


# MAIN LOOP ------------------------------------------------------------------------------------------------------------
continuer = 1
while continuer:
	# On remet ces variables à 1 à chaque tour de boucle
	continuer_jeu = 1
	continuer_accueil = 1
	level_launched = 1
	# BOUCLE D'ACCUEIL ------------------------------------------------------------------------------------------------
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
			if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				continuer_accueil = 0
				level_launched = 0
				continuer_jeu = 0
				continuer = 0
			# MOUSE LEFT CLICK UP
			choix = 0
			if event.type == pygame.MOUSEBUTTONUP and event.button == 1:		# If button UP
				if b1.imageRect.collidepoint(mouse):
					b1.stick(scr, "press")
					continuer_accueil = 0
					choix = 'maps/n1'
				if b2.imageRect.collidepoint(mouse):
					b2.stick(scr, "press")
					continuer_accueil = 0
					continuer_jeu = 0
					continuer = 0
		pygame.display.flip()
# ---------------------------------------------------------------------------------------------------------------------
# Features Levels
# ---------------------------------------------------------------------------------------------------------------------
	# Loading background
	fond = pygame.image.load(image_fond).convert()
	fond.fill(black)
	# Level generation
	level = Level(choix)
	level.generate()
	level.display(scr)
	# player generation
	mac_giver = Player(image_player, level)
	# BOUCLE DE JEU ---------------------------------------------------------------------------------------------------
	win_lose = False
	while continuer_jeu:
		# Loop speed limitation
		pygame.time.Clock().tick(30)
		mouse = pygame.mouse.get_pos()

		for event in pygame.event.get():
			# Si l'utilisateur quitte, on met la variable qui continue le jeu
			# ET la variable générale à 0 pour fermer la fenêtre
			if event.type == pygame.QUIT:
				continuer_jeu = 0
				continuer = 0
			elif event.type == pygame.KEYDOWN:
				# Si l'utilisateur presse Echap ici, on revient seulement au menu
				if event.key == pygame.K_ESCAPE:
					continuer_jeu = 0
				# Touches de déplacement de Donkey Kong
				elif event.key == pygame.K_RIGHT and win_lose == False:
					mac_giver.move('droite')
				elif event.key == pygame.K_LEFT and win_lose == False:
					mac_giver.move('gauche')
				elif event.key == pygame.K_UP and win_lose == False:
					mac_giver.move('haut')
				elif event.key == pygame.K_DOWN and win_lose == False:
					mac_giver.move('bas')			
			
			# Affichages aux nouvelles positions
			scr.blit(fond, (0, 0))
			level.display(scr)
			scr.blit(mac_giver.image_player, (mac_giver.x, mac_giver.y))  # dk.direction = l'image dans la bonne \
			# direction
			pygame.display.flip()
			# End------------------------------------------------------------------------------------------------------
			# Win
			if level.structure[mac_giver.case_y][mac_giver.case_x] == 'a':
				win_lose = True
				b_win.stick(scr)
				b_menu.stick(scr)
				b2.stick(scr)
			# Lose
			if level.structure[mac_giver.case_y][mac_giver.case_x] == 'g' and len(mac_giver.bag) != 3:
				win_lose = True
				b_lose.stick(scr)
				b_menu.stick(scr)
				b2.stick(scr)
			# MENU
			if b_menu.imageRect.collidepoint(mouse) and win_lose:		# win_lose true if game finished
				b_menu.stick(scr, "press")
			# QUIT
			if b2.imageRect.collidepoint(mouse) and win_lose:
				b2.stick(scr, "press")
			# MOUSE LEFT CLICK UP---------------------------------------------------------------------------------------
			if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and win_lose:  # If button UP
				if b_menu.imageRect.collidepoint(mouse):
					b_menu.stick(scr, "press")
					continuer_jeu = 0
				if b2.imageRect.collidepoint(mouse):
					b2.stick(scr, "press")
					continuer_accueil = 0
					continuer_jeu = 0
					continuer = 0

			pygame.display.flip()

