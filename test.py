import pygame
from pygame.locals import *


pygame.init()

#Ouverture de la fen�tre Pygame
fenetre = pygame.display.set_mode((640, 480))

#Chargement et collage du fond
fond = pygame.image.load("icons/background.jpg").convert()
fond = pygame.transform.scale(fond, (640, 480))
fenetre.blit(fond, (0,0))

#Chargement et collage du volant
perso = pygame.image.load("icons/steering-wheel.png").convert_alpha()
perso = pygame.transform.scale(perso, (120, 120))
position_perso = perso.get_rect()
position_perso.center = 320,400

#Chargement et collage du cligno_droit
clid = pygame.image.load("icons/NIL.png").convert_alpha()
position_clid = clid.get_rect()
position_clid.center = 590,430

#Chargement et collage du cligno_gauche
clig = pygame.image.load("icons/NIL.png").convert_alpha()
position_clig = clig.get_rect()
position_clig.center = 590,50

#Chargement et collage du rapport
rap = pygame.image.load("icons/one.png").convert_alpha()
position_rap = rap.get_rect()
position_rap.center = 490,340


fenetre.blit(perso, position_perso)
#fenetre.blit(clid, position_clid)

#Rafra�chissement de l'�cran
pygame.display.flip()


#On compte les joysticks
nb_joysticks = pygame.joystick.get_count()
#Et on en cr�e un s'il y a en au moins un
if nb_joysticks > 0:
    mon_joystick = pygame.joystick.Joystick(0)
    mon_joystick.init() #Initialisation


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
etat=0
x=0
val=0
vitesse=0
tour=1000
rapport=1
continuer = 1
while continuer :
    for event in pygame.event.get():	#Attente des �v�nements
        if event.type == QUIT:
            pygame.quit()
            continuer = 0
        if event.type == JOYAXISMOTION:
            if event.axis == 0:
                if event.value > 0.20 and event.value <= 0.4:
                    perso = pygame.image.load("icons/steering-wheel.png").convert_alpha()
                    perso = pygame.transform.scale(perso, (120, 120))
                    perso = pygame.transform.rotate(perso, -22)
                    position_perso = perso.get_rect()
                    position_perso.center = 320,400                    
                elif event.value > 0.4 and event.value <= 0.6:
                    perso = pygame.image.load("icons/steering-wheel.png").convert_alpha()
                    perso = pygame.transform.scale(perso, (120, 120))
                    perso = pygame.transform.rotate(perso, -45)
                    position_perso = perso.get_rect()
                    position_perso.center = 320,400
                elif event.value > 0.6 and event.value <= 0.8:
                    perso = pygame.image.load("icons/steering-wheel.png").convert_alpha()
                    perso = pygame.transform.scale(perso, (120, 120))
                    perso = pygame.transform.rotate(perso, -67)
                    position_perso = perso.get_rect()
                    position_perso.center = 320,400
                elif event.value > 0.8 and event.value <= 1:
                    perso = pygame.image.load("icons/steering-wheel.png").convert_alpha()
                    perso = pygame.transform.scale(perso, (120, 120))
                    perso = pygame.transform.rotate(perso, -90)
                    position_perso = perso.get_rect()
                    position_perso.center = 320,400
                    x=0
                elif event.value <= 0.20 and event.value >= -0.20:
                    perso = pygame.image.load("icons/steering-wheel.png").convert_alpha()
                    perso = pygame.transform.scale(perso, (120, 120))
                    position_perso = perso.get_rect()
                    position_perso.center = 320,400
                if event.value < -0.20 and event.value >= -0.4:
                    perso = pygame.image.load("icons/steering-wheel.png").convert_alpha()
                    perso = pygame.transform.scale(perso, (120, 120))
                    perso = pygame.transform.rotate(perso, 22)
                    position_perso = perso.get_rect()
                    position_perso.center = 320,400
                elif event.value < -0.4 and event.value >= -0.6:
                    perso = pygame.image.load("icons/steering-wheel.png").convert_alpha()
                    perso = pygame.transform.scale(perso, (120, 120))
                    perso = pygame.transform.rotate(perso, 45)
                    position_perso = perso.get_rect()
                    position_perso.center = 320,400
                elif event.value < -0.6 and event.value >= -0.8:
                    perso = pygame.image.load("icons/steering-wheel.png").convert_alpha()
                    perso = pygame.transform.scale(perso, (120, 120))
                    perso = pygame.transform.rotate(perso, 67)
                    position_perso = perso.get_rect()
                    position_perso.center = 320,400
                elif event.value < -0.8 and event.value >= -1:
                    perso = pygame.image.load("icons/steering-wheel.png").convert_alpha()
                    perso = pygame.transform.scale(perso, (120, 120))
                    perso = pygame.transform.rotate(perso, 90)
                    position_perso = perso.get_rect()
                    position_perso.center = 320,400
                    x=0


            if event.axis == 2:
                if event.value < -0.1 and event.value >= -1:
                    #print(mon_joystick.get_axis(2))#accelerer
                    tour = tour - mon_joystick.get_axis(2)* 60
                    print(tour)
                elif event.value > 0.1 and event.value <= 1:
                    if tour > 1060:
                        tour = tour - mon_joystick.get_axis(2)* 60
                    else:
                        tour=1000
                    print(tour)
                
                    
        #if event.type == JOYBUTTONDOWN and event.button == 1:
        #    digitalWrite(LED, HIGH)
        #    delay(1000)
        if event.type == JOYBUTTONDOWN:
            #while not (event.type == JOYBUTTONUP):
            if event.button == 1:
                x=1
            elif event.button == 2:
                x=2
            elif event.button == 0:
                x=0

            else:
                if event.button == 5:
                    if rapport < 5 and tour > 2000:
                        rapport = rapport + 1
                        tour = tour - 1000
                        print(rapport)
                if event.button == 4:
                    if rapport > 1:
                        rapport = rapport - 1
                        tour = tour + 1000
                        print(rapport)
            
        if (x==1):            
            clid = pygame.image.load("icons/right-arrow.png").convert_alpha()
            position_clid = clid.get_rect()
            position_clid.center = 590,430
            clig = pygame.image.load("icons/NIL.png").convert_alpha()
            position_clig = clig.get_rect()
            position_clig.center = 590,50
        elif (x==2):
            clid = pygame.image.load("icons/NIL.png").convert_alpha()
            position_clid = clid.get_rect()
            position_clid.center = 590,430
            clig = pygame.image.load("icons/right-arrow(1).png").convert_alpha()
            position_clig = clig.get_rect()
            position_clig.center = 50,430
        elif (x==0):
            clid = pygame.image.load("icons/NIL.png").convert_alpha()
            position_clid = clid.get_rect()
            position_clid.center = 590,430
            clig = pygame.image.load("icons/NIL.png").convert_alpha()
            position_clig = clig.get_rect()
            position_clig.center = 590,50


        if (rapport == 1):
            rap = pygame.image.load("icons/one.png").convert_alpha()
            position_rap = rap.get_rect()
            position_rap.center = 490,340
        if (rapport == 2):
            rap = pygame.image.load("icons/two.png").convert_alpha()
            position_rap = rap.get_rect()
            position_rap.center = 490,340
        if (rapport == 3):
            rap = pygame.image.load("icons/three.png").convert_alpha()
            position_rap = rap.get_rect()
            position_rap.center = 490,340
        if (rapport == 4):
            rap = pygame.image.load("icons/four.png").convert_alpha()
            position_rap = rap.get_rect()
            position_rap.center = 490,340
        if (rapport == 5):
            rap = pygame.image.load("icons/five.png").convert_alpha()
            position_rap = rap.get_rect()
            position_rap.center = 490,340
            
            
    #Re-collage
    fenetre.blit(fond, (0,0))
    fenetre.blit(perso, position_perso)
    fenetre.blit(clid, position_clid)
    fenetre.blit(clig, position_clig)
    fenetre.blit(rap, position_rap)
    #Rafraichissement
    pygame.display.flip()
