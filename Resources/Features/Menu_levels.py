# coding:utf-8
from classes import *

# LOOP LEVEL ------------------------------------------------------------------------------------------------------
	level_launched = 1
	while level_launched:
		# Speed limitation and mouse position
		pygame.time.Clock().tick(100)
		mouse = pygame.mouse.get_pos()
		scr.blit(accueil, (0, 0))
		b_level_title.stick(scr)
		b_level1.stick(scr)
		b_level2.stick(scr)
		b_back.stick(scr)

		# if mouse on buttons
		if b_level1.imageRect.collidepoint(mouse):  # choice level 1
			b_level1.stick(scr, "press")
		if b_level2.imageRect.collidepoint(mouse):
			b_level2.stick(scr, "press")
		if b_back.imageRect.collidepoint(mouse):
			b_back.stick(scr, "press")

		for event in pygame.event.get():
			print("TEST EVENT")
			# Exit conditions
			if event.type == pygame.QUIT:
				continuer_jeu = 0
				continuer = 0
				level_launched = 0
			elif event.type == pygame.KEYDOWN:
				# Si l'utilisateur presse Echap ici, on revient seulement au menu precedent
				if event.key == pygame.K_ESCAPE:
					continuer_jeu = 0
					level_launched = 0
			# MOUSE LEFT CLICK UP
			if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # If button UP
				print("TEST RELEVE")
				if b_level1.imageRect.collidepoint(mouse):
					b_level1.stick(scr, "press")
					choix = 'maps/n1'
					level_launched = 0
				if b_level2.imageRect.collidepoint(mouse):
					b_level2.stick(scr, "press")
					choix = 'maps/n2'
					level_launched = 0
				if b_back.imageRect.collidepoint(mouse):
					b_back.stick(scr, "press")
					level_launched = 0
					continuer_jeu = 0
		pygame.display.flip()