import pygame
from pygame.locals import *


pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))

#Chargement et collage du fond
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))

#Chargement et collage du personnage
perso = pygame.image.load("/Python27/icons/steering-wheel.png").convert_alpha()
position_perso = perso.get_rect()
position_perso.center = 320,240
#perso.center = 320,240

fenetre.blit(perso, position_perso)
#fenetre.blit(perso)

#Rafraîchissement de l'écran
pygame.display.flip()

pygame.key.set_repeat(400, 30)

#On compte les joysticks
nb_joysticks = pygame.joystick.get_count()
#Et on en crée un s'il y a en au moins un
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
    for event in pygame.event.get():	#Attente des événements
        if event.type == QUIT:
            pygame.quit()
            continuer = 0        
        if event.type == JOYAXISMOTION:            
            if event.axis == 0:
                if event.value > 0.20 and event.value <= 1:                
                    val2 = mon_joystick.get_axis(0)
                    print(val2)
                    print("ancien", val)
                    print("diff", val2-val)
                    if val2>val:
                        #position_perso = position_perso.move((val2-val)*100,0)
                        perso = pygame.image.load("/Python27/icons/steering-wheel.png").convert_alpha()
                        perso=pygame.transform.rotate(perso, -(val2-val)*100)
                        position_perso = perso.get_rect()
                        position_perso.center = 320,240
                        fenetre.blit(perso, position_perso)
                        #perso = perso.transform((val2-val)*100)
                        val=mon_joystick.get_axis(0)
                    else:
                        position_perso = position_perso.move((val2-val)*100,0)
                        val=mon_joystick.get_axis(0)
                elif event.value <= 0.20 and event.value >= -0.20:
                    position_perso.center = 320,240
                else:
                    val2 = mon_joystick.get_axis(0)
                    print(val2)
                    print("ancien", val)
                    print("diff", val2-val)
                    if val2<val:
                        position_perso = position_perso.move((val2-val)*100,0)
                        val=mon_joystick.get_axis(0)
                    else:
                        position_perso = position_perso.move((val2-val)*100,0)
                        val=mon_joystick.get_axis(0)
                    

                    
                    
                
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
    #Rafraichissement
    pygame.display.flip()
