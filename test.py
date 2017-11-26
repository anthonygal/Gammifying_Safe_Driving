import random
import sys
from threading import Thread
import time
import pygame
from pygame.locals import *


pygame.init()

#Ouverture de la fenï¿½tre Pygame
fenetre = pygame.display.set_mode((640, 480))

#Chargement et collage du fond
fond = pygame.image.load("icons/background.jpg").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
perso = pygame.image.load("icons/steering-wheel.png").convert_alpha()
position_perso = perso.get_rect()
position_perso.center = 320,240
fenetre.blit(perso, position_perso)

#Vitesse
font = pygame.font.Font(None, 32) 
vitesse = 0
TRM = 0

fenetre.fill(Color("black"),(71,73,80,70))
text = font.render(str(TRM),1,(255,255,255))
fenetre.blit(text, (100, 100))

class augmenteTRM(Thread):
    def __init__(self, temps):
        Thread.__init__(self)
        self.temps = temps
        self.running = False

    def run(self):
        global TRM
        global text
        global font
        """Le code que le thread devra exécuter."""
        self.running = True
        # scrutation du buffer d'entree 
        while self.running:
            time.sleep(self.temps)
            if self.running:
                TRM += 1
                fenetre.fill(Color("black"),(71,73,80,70))
                text = font.render(str(TRM),1,(255,255,255))
                fenetre.blit(text, (100, 100))
                pygame.display.flip()
 
    def stop(self):
        self.running = False


#Rafraï¿½chissement de l'ï¿½cran
pygame.display.flip()

pygame.key.set_repeat(400, 30)

#On compte les joysticks
nb_joysticks = pygame.joystick.get_count()
#Et on en crï¿½e un s'il y a en au moins un
if nb_joysticks > 0:
    mon_joystick = pygame.joystick.Joystick(0)
    mon_joystick.init() #Initialisation
    print("Axes :", mon_joystick.get_numaxes())
    print("Boutons :", mon_joystick.get_numbuttons())
    print("Trackballs :", mon_joystick.get_numballs())
    print("Hats :", mon_joystick.get_numhats())
##
##continuer = 1
##while continuer:
##    for event in pygame.event.get():
##        if event.type == QUIT:
##            continuer = 0
##            pygame.quit()
##
##        if event.type == JOYAXISMOTION:
##            if event.axis == 0 and event.value > 0.1 and event.value <= 1:
##                val = mon_joystick.get_axis(0)
##                val = val-0.1
##                print(val)
##                position_perso = position_perso.move(val,0)
##
##
##    #Re-collage
##    fenetre.blit(fond, (0,0))
##    fenetre.blit(perso, position_perso)
##    #Rafraichissement
##    pygame.display.flip()


##        if event.type == JOYBUTTONDOWN and event.button == 0:
##            print("A")
##        if event.type == JOYBUTTONDOWN and event.button == 1:
##            print("B")
##        if event.type == JOYBUTTONDOWN and event.button == 2:
##            print("X")
##        if event.type == JOYBUTTONDOWN and event.button == 3:
##            print("Y")
##        if event.type == JOYBUTTONDOWN and event.button == 4:
##            print("LB")
##        if event.type == JOYBUTTONDOWN and event.button == 5:
##            print("RB")
##        if event.type == JOYBUTTONDOWN and event.button == 6:
##            print("select")
##        if event.type == JOYBUTTONDOWN and event.button == 7:
##            print("start")
##        if event.type == JOYBUTTONDOWN and event.button == 8:
##            print("enfoncer joystick gauche")
##        if event.type == JOYBUTTONDOWN and event.button == 9:
##            print("enfoncer joystick droit")
##
##        if event.type == JOYAXISMOTION:
##            if event.axis == 0 and event.value > 0.1 and event.value <= 1:
##                print(mon_joystick.get_axis(0))#droit
##            if event.axis == 0 and event.value < -0.1 and event.value >= -1:
##                print(mon_joystick.get_axis(0))#gauche
##            if event.axis == 2 and event.value < -0.1 and event.value >= - 1:
##                print(mon_joystick.get_axis(2))#accelerer
##            if event.axis == 2 and event.value > 0.1 and event.value <= 1:
##                print(mon_joystick.get_axis(2))#frener

        #if event.type == JOYAXISMOTION and event.axis == 2:
        #   print(mon_joystick.get_axis(2))



#BOUCLE INFINIE
val=0
continuer = 1
while continuer:
    for event in pygame.event.get():	#Attente des ï¿½vï¿½nements
        if event.type == QUIT:
            pygame.quit()
            continuer = 0
        if event.type == JOYAXISMOTION:
            if event.axis == 0:
                if event.value > 0.20 and event.value <= 0.4:
                    perso = pygame.image.load("icons/steering-wheel.png").convert_alpha()
                    perso = pygame.transform.rotate(perso, -22)
                    position_perso = perso.get_rect()
                    position_perso.center = (320,240)
                    fenetre.blit(perso, position_perso)
                elif event.value > 0.4 and event.value <= 0.6:
                    perso = pygame.image.load("icons/steering-wheel.png").convert_alpha()
                    perso = pygame.transform.rotate(perso, -45)
                    position_perso = perso.get_rect()
                    position_perso.center = (320,240)
                    fenetre.blit(perso, position_perso)
                elif event.value > 0.6 and event.value <= 0.8:
                    perso = pygame.image.load("icons/steering-wheel.png").convert_alpha()
                    perso = pygame.transform.rotate(perso, -67)
                    position_perso = perso.get_rect()
                    position_perso.center = (320,240)
                    fenetre.blit(perso, position_perso)
                elif event.value > 0.8 and event.value <= 1:
                    perso = pygame.image.load("icons/steering-wheel.png").convert_alpha()
                    perso = pygame.transform.rotate(perso, -90)
                    position_perso = perso.get_rect()
                    position_perso.center = (320,240)
                    fenetre.blit(perso, position_perso)
                elif event.value <= 0.20 and event.value >= -0.20:
                    perso = pygame.image.load("icons/steering-wheel.png").convert_alpha()
                    position_perso = perso.get_rect()
                    position_perso.center = (320,240)
                    fenetre.blit(perso, position_perso)
                if event.value < -0.20 and event.value >= -0.4:
                    perso = pygame.image.load("icons/steering-wheel.png").convert_alpha()
                    perso = pygame.transform.rotate(perso, 22)
                    position_perso = perso.get_rect()
                    position_perso.center = (320,240)
                    fenetre.blit(perso, position_perso)
                elif event.value < -0.4 and event.value >= -0.6:
                    perso = pygame.image.load("icons/steering-wheel.png").convert_alpha()
                    perso = pygame.transform.rotate(perso, 45)
                    position_perso = perso.get_rect()
                    position_perso.center = (320,240)
                    fenetre.blit(perso, position_perso)
                elif event.value < -0.6 and event.value >= -0.8:
                    perso = pygame.image.load("icons/steering-wheel.png").convert_alpha()
                    perso = pygame.transform.rotate(perso, 67)
                    position_perso = perso.get_rect()
                    position_perso.center = (320,240)
                    fenetre.blit(perso, position_perso)
                elif event.value < -0.8 and event.value >= -1:
                    perso = pygame.image.load("icons/steering-wheel.png").convert_alpha()
                    perso = pygame.transform.rotate(perso, 90)
                    position_perso = perso.get_rect()
                    position_perso.center = (320,240)
                    fenetre.blit(perso, position_perso)
            if event.axis == 2:
                if event.value < -0.2 and event.value >= -0.4:
                    perso = pygame.image.load("icons/steering-wheel.png").convert_alpha()
                    perso = pygame.transform.rotate(perso, -22)
                    position_perso = perso.get_rect()
                    position_perso.center = (320,240)
                    fenetre.blit(perso, position_perso)
                if event.value > 0.20 and event.value <= 0.4:
                    perso = pygame.image.load("icons/steering-wheel.png").convert_alpha()
                    perso = pygame.transform.rotate(perso, -22)
                    position_perso = perso.get_rect()
                    position_perso.center = (320,240)
                    fenetre.blit(perso, position_perso)





##            if event.key == K_DOWN:
##                position_perso = position_perso.move(0,3)
##            if event.key == K_RIGHT:
##                position_perso = position_perso.move(3,0)
##            if event.key == K_LEFT:
##                position_perso = position_perso.move(-3,0)
##            if event.key == K_UP:
##              position_perso = position_perso.move(0,-3)
    #Re-collage
    fenetre.blit(fond, (0,0))
    fenetre.blit(perso, position_perso)
    fenetre.blit(text, (100, 100))
    #Rafraichissement
    pygame.display.flip()
