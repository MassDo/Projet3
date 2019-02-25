# coding:utf-8
""" Classes du jeu Mc giver """ 
 
import pygame
import random
from inputs import *

# ---------------------------------------------------------------------------------------------------------------------
class Level:
    """class for the creation of a level"""

    def __init__(self, file):
        self.file = file
        self.structure = []
# ---------------------------------------------------------------------------------------------------------------------
    def generate(self):

        """generation from the map file of a structure of characters associated with the sprites"""

        with open(self.file + ".txt", "r") as var_fichier:
            structure_niveau = []
            # On parcourt les lignes du fichier
            for ligne in var_fichier:
                ligne_niveau = []
                # On parcourt les sprites (lettres) contenus dans le fichier
                for sprite in ligne:
                    # On ignore les "\n" de fin de ligne
                    if sprite != '\n':
                        # On ajoute le sprite à la liste de la ligne
                        ligne_niveau.append(sprite)
                # On ajoute la ligne à la liste du niveau
                structure_niveau.append(ligne_niveau)
            # On sauvegarde cette structure
            self.structure = structure_niveau
            # Ajout des objets au hasard
            k = 0
            while k < 3:
                ligne = random.randrange(max_sprites_size)
                column = random.randrange(max_sprites_size)
                if self.structure[ligne][column] == "c":
                    self.structure[ligne][column] = objects_sprites[k]
                    k += 1
# ---------------------------------------------------------------------------------------------------------------------
    def display(self, screen):

        """ display of the level from structure and sprites"""

        mur = pygame.image.load(image_mur).convert()
        depart = pygame.image.load(image_depart).convert()
        arrivee = pygame.image.load(image_arrivee).convert_alpha()
        garde = pygame.image.load(image_garde).convert_alpha()
        aiguille = pygame.image.load(image_aiguille).convert_alpha()
        tube = pygame.image.load(image_tube).convert_alpha()

        seringue = pygame.image.load(image_seringue).convert_alpha()

        # On parcourt la liste du niveau
        num_ligne = 0
        for ligne in self.structure:
            # On parcourt les listes de lignes
            num_case = 0
            for sprite in ligne:
                # On calcule la position réelle en pixels
                x = num_case * sprite_size_pixel
                y = num_ligne * sprite_size_pixel
                if sprite == 'm':		   # m = Mur
                    screen.blit(mur, (x, y))
                elif sprite == 'd':		   # d = Départ
                    screen.blit(depart, (x, y))
                elif sprite == 'a':		   # a = Arrivée
                    screen.blit(arrivee, (x, y))
                elif sprite == 'g':		   # g = garde
                    screen.blit(garde, (x, y))
                elif sprite == 'l':		   # l = aiguille
                    screen.blit(aiguille, (x, y))
                elif sprite == 't':		   # t = tube
                    screen.blit(tube, (x, y))
                elif sprite == 's':		   # s = sortie
                    screen.blit(seringue, (x, y))
                num_case += 1
            num_ligne += 1

# ---------------------------------------------------------------------------------------------------------------------
class Player:

    """class creating player"""

    def __init__(self, image_player, level):
        # Sprites du personnage
        self.image_player = pygame.image.load(image_player).convert_alpha()
        # Position du personnage en cases et en pixels
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        # Niveau dans lequel le personnage se trouve
        self.level = level
        # bag of the player
        self.bag = []
# ---------------------------------------------------------------------------------------------------------------------
    def move(self, direction):

        """moving player"""

        # Déplacement vers la droite
        if direction == 'droite':
            # Pour ne pas dépasser l'écran
            if self.case_x < (max_sprites_size - 1):
                # On vérifie que la case de destination n'est pas un mur
                if self.level.structure[self.case_y][self.case_x+1] != 'm':
                    # Déplacement d'une case
                    self.case_x += 1
                    # Calcul de la position "réelle" en pixel
                    self.x = self.case_x * sprite_size_pixel

        # Déplacement vers la gauche
        if direction == 'gauche':
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x-1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x * sprite_size_pixel

        # Déplacement vers le haut
        if direction == 'haut':
            if self.case_y > 0:
                if self.level.structure[self.case_y-1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y = self.case_y * sprite_size_pixel

        # Déplacement vers le bas
        if direction == 'bas':
            if self.case_y < (max_sprites_size - 1):
                if self.level.structure[self.case_y+1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y = self.case_y * sprite_size_pixel

        # Si objet recupération
        if self.level.structure[self.case_y][self.case_x] in objects_sprites:
            # ajout de l'objet dans le sac
            self.bag.append(self.level.structure[self.case_y][self.case_x])
            # suppression de l'objet de la carte
            self.level.structure[self.case_y][self.case_x] = ""

        # Si gardien et pas les 4 objets alors mort
        if self.level.structure[self.case_y][self.case_x] == "g":
            if len(self.bag) != 3:
                # FIN DE BOUCLE #
                continuer_jeu = 0
                print("C'est perdu !")

        # Arrivée
        if self.level.structure[self.case_y][self.case_x]== "g" and len(self.bag) == 3 :
            print("C'est GAGNE !")
            ### FIN DE BOUCLE ###

# ---------------------------------------------------------------------------------------------------------------------
class Button:

    """ class d'objet boutton cliquables, placé, de taille prédéfinie avec texte centré """

    def __init__(self, text, color, fontsize, emplacement, picture, picturePress, blankColor = None):
        """ Button with attributs text, emplacement, pict, pict when the button is pressed"""

        font = pygame.font.SysFont("arial", fontsize, bold, italique)
        self.text = text
        self.color = color
        self.font_size = fontsize
        self.textSurf = font.render(self.text, True, self.color)
        self.textRect = self.textSurf.get_rect()
        self.emplacement = emplacement
        self.picture = picture
        self.picturePress = picturePress
        self.image = pygame.image.load(self.picturePress).convert()
        self.imageRect = self.image.get_rect().move(emplacement)
        self.positionText = ()
        self.blankColor = blankColor
        # Center the text into the button
        xi, yi, W, H = self.imageRect.x, self.imageRect.y, self.imageRect.w, self.imageRect.height
        w, h = self.textRect.w, self.textRect.h
        # final coordinates of the text rect
        self.xf = xi + (W/2) - (w/2)
        self.yf = yi + (H/2) - (h/2)
        self.positionText = self.xf, self.yf
# ---------------------------------------------------------------------------------------------------------------------
    def stick(self, surface, press = None):
        """stick the button to the surface, pressed or not"""

        font = pygame.font.SysFont("arial", self.font_size, bold, italique)

        # if the button is pressed
        if press == "press":
            self.image = pygame.image.load(self.picturePress).convert()
            self.image.set_colorkey(self.blankColor)
            self.imageRect = self.image.get_rect().move(self.emplacement)
            surface.blit(self.image, self.imageRect)
            if len(self.text.splitlines()) != 1:        # If the text got multiple lines
                xf, yf = self.imageRect.topleft
                for ligne in self.text.splitlines():
                    print(xf, yf)
                    surface.blit(font.render(ligne, True, self.color), (xf, yf))
                    yf += self.font_size
            else:
                surface.blit(self.textSurf, self.positionText)      # If text is just one word
        else:
            self.image = pygame.image.load(self.picture).convert()
            self.image.set_colorkey(self.blankColor)
            self.imageRect = self.image.get_rect().move(self.emplacement)
            surface.blit(self.image, self.imageRect)
            if len(self.text.splitlines()) != 1:
                xf, yf = self.imageRect.topleft
                for ligne in self.text.splitlines():
                    surface.blit(font.render(ligne, True, self.color), (xf, yf))
                    yf += self.font_size
            else:
                surface.blit(self.textSurf, self.positionText)







