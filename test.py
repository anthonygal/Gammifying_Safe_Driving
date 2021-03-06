import random
import sys
import time
from threading import *
import pygame
from pygame.locals import *

score = 0
nbr_action = 0
etat=0
x=0
#val=0
rapport=1
thread = 0
good = -1

def clignotant(time_clignotant, time_turn):
	global score
	global nbr_action
	global good
	score = score * nbr_action / (nbr_action + 1)
	nbr_action = nbr_action + 1
	delta = time_turn - time_clignotant
	if(time_clignotant == 0):
		score = score + 0/nbr_action
		good = 0
	if (delta < 1):
		score = score + 25/nbr_action
		good = 1
	elif (delta > 1) and (delta <= 2):
		score = score + 50/nbr_action
		good = 1
	elif (delta > 2) and (delta <= 3):
		score = score + 100/nbr_action
		good = 3
	elif (delta > 3) and (delta <= 15):
		score = score + 75/nbr_action
		good = 2


def rapport_tr_aug(tr_min):
	global score
	global nbr_action
	global good
	score = score * nbr_action / (nbr_action + 1)
	nbr_action = nbr_action + 1
	if (tr_min < 2100) or (tr_min > 2900):
		score = score + 0/nbr_action
		good = 0
	elif (tr_min < 2200) or (tr_min > 2800):
		score = score + 25/nbr_action
		good = 1
	elif (tr_min < 2300) or (tr_min > 2700):
		score = score + 50/nbr_action
		good = 1
	elif (tr_min < 2400) or (tr_min > 2600):
		score = score + 75/nbr_action
		good = 2
	else:
		score = score + 100/nbr_action
		good = 3

def rapport_tr_dim(tr_min):
	global score
	global nbr_action
	global good
	score = score * nbr_action / (nbr_action + 1)
	nbr_action = nbr_action + 1
	if (tr_min < 1100) or (tr_min > 1900):
		score = score + 0/nbr_action
		good = 0
	elif (tr_min < 1200) or (tr_min > 1800):
		score = score + 25/nbr_action
		good = 1
	elif (tr_min < 1300) or (tr_min > 1700):
		score = score + 50/nbr_action
		good = 1
	elif (tr_min < 1400) or (tr_min > 1600):
		score = score + 75/nbr_action
		good = 2
	else:
		score = score + 100/nbr_action
		good = 3

pygame.init()

#Ouverture de la fen�tre Pygame
fenetre = pygame.display.set_mode((640, 480))

#Chargement et collage du fond
fond = pygame.image.load("icons/background4.jpg").convert()
fond = pygame.transform.scale(fond, (640, 480))
fenetre.blit(fond, (0,0))

#Chargement et collage du volant
perso = pygame.image.load("icons/steering-wheel.png").convert_alpha()
perso = pygame.transform.scale(perso, (120, 120))
position_perso = perso.get_rect()

#position_perso.center = 320,240
position_perso.center = 320,400
fenetre.blit(perso, position_perso)


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
position_rap.center = 490,350

#Chargement et collage de l'�moji
emo = pygame.image.load("icons/NIL.png").convert_alpha()
position_emo = emo.get_rect()
position_emo.center = 490,50

#TRM
TRM = 1000
font = pygame.font.Font(None, 32)
fenetre.fill(Color("black"),(50,330,80,60))
text = font.render(str(TRM),1,(255,255,255))
fenetre.blit(text, (65, 350))
#font2 = pygame.font.Font(None, 18)
text2 = font.render("tr/min",1,(0,0,0))
fenetre.blit(text2, (70, 390))

#Vitesse
vit = 0
fenetre.fill(Color("black"),(160,330,80,60))
text3 = font.render(str(vit),1,(255,255,255))
fenetre.blit(text3, (175, 350))
text4 = font.render("km/h",1,(0,0,0))
fenetre.blit(text4, (180, 390))

#Score
fenetre.fill(Color("black"),(240,30,150,50))
text5 = font.render("Score : "+str(score),1,(255,255,255))
fenetre.blit(text5, (250, 45))

class augmenteTRM(Thread):
    def __init__(self, temps):
        Thread.__init__(self)
        self.temps = temps
        self.running = False

    def run(self):
        global TRM
        global text
        global font
        """Le code que le thread devra ex�cuter."""
        self.running = True
        # scrutation du buffer d'entree
        while self.running:
            time.sleep(self.temps)
            if self.running:
                if(TRM<8000):
                    TRM += 1
                fenetre.fill(Color("black"),(50,330,80,60))
                text = font.render(str(TRM),1,(255,255,255))
                fenetre.blit(text, (65, 350))
                pygame.display.flip()

    def stop(self):
        self.running = False

class diminuerTRM(Thread):
    def __init__(self, temps):
        Thread.__init__(self)
        self.temps = temps
        self.running = False

    def run(self):
        global TRM
        global text
        global font
        """Le code que le thread devra ex�cuter."""
        self.running = True
        # scrutation du buffer d'entree
        while self.running:
            time.sleep(self.temps)
            if self.running:
                if(TRM>1000):
                    TRM -= 1
                fenetre.fill(Color("black"),(50,330,80,60))
                text = font.render(str(TRM),1,(255,255,255))
                fenetre.blit(text, (65, 350))
                pygame.display.flip()

    def stop(self):
        self.running = False

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
continuer = 1
start_timed = 0
start_timeg = 0
end_time = 0

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
                    end_time = time.time()
                    t = clignotant(start_timed, end_time)
                    start_timed=0
                    print(score)
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
                    end_time = time.time()
                    t = clignotant(start_timeg, end_time)
                    start_timeg=0
                    print(score)
                    perso = pygame.image.load("icons/steering-wheel.png").convert_alpha()
                    perso = pygame.transform.scale(perso, (120, 120))
                    perso = pygame.transform.rotate(perso, 90)
                    position_perso = perso.get_rect()
                    position_perso.center = 320,400
                    x=0

        if event.type == JOYBUTTONDOWN:
            #while not (event.type == JOYBUTTONUP):
            if event.button == 1:
                #global start_time
                x=1
                start_timed = time.time()
            elif event.button == 2:
                x=2
                start_timeg = time.time()
            elif event.button == 0:
                x=0

            else:
                if event.button == 5:
                    if rapport < 5 and TRM > 2000:
                        rapport = rapport+1
                        rapport_tr_aug(TRM)
                        TRM = TRM - 1000
                        print(rapport)
                if event.button == 4:
                    if rapport > 1:
                        rapport = rapport - 1
                        rapport_tr_dim(TRM)
                        TRM = TRM + 1000
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
            position_rap.center = 490,350
        if (rapport == 2):
            rap = pygame.image.load("icons/two.png").convert_alpha()
            position_rap = rap.get_rect()
            position_rap.center = 490,350
        if (rapport == 3):
            rap = pygame.image.load("icons/three.png").convert_alpha()
            position_rap = rap.get_rect()
            position_rap.center = 490,350
        if (rapport == 4):
            rap = pygame.image.load("icons/four.png").convert_alpha()
            position_rap = rap.get_rect()
            position_rap.center = 490,350
        if (rapport == 5):
            rap = pygame.image.load("icons/five.png").convert_alpha()
            position_rap = rap.get_rect()
            position_rap.center = 490,350

        if event.type == JOYAXISMOTION:
            if event.axis == 2:
                if event.value > 0.2 and event.value <= 0.4:
                    if(thread!=0):
                        thread.stop()
                    thread = diminuerTRM(0.025)
                    thread.start()
                if event.value > 0.4 and event.value <= 0.6:
                    if(thread!=0):
                        thread.stop()
                    thread = diminuerTRM(0.012)
                    thread.start()
                if event.value > 0.4 and event.value <= 0.8:
                    if(thread!=0):
                        thread.stop()
                    thread = diminuerTRM(0.006)
                    thread.start()
                if event.value > 0.8 and event.value <= 1:
                    if(thread!=0):
                        thread.stop()
                    thread = diminuerTRM(0.002)
                    thread.start()
                if event.value >= -0.2 and event.value <= 0.2:
                    if(thread!=0):
                        thread.stop()
                    thread = diminuerTRM(0.5)
                    thread.start()
                if event.value < -0.2 and event.value >= -0.4:
                    if(thread!=0):
                        thread.stop()
                    thread = augmenteTRM(0.025)
                    thread.start()
                if event.value < -0.4 and event.value >= -0.6:
                    if(thread!=0):
                        thread.stop()
                    thread = augmenteTRM(0.012)
                    thread.start()
                if event.value < -0.6 and event.value >= -0.8:
                    if(thread!=0):
                        thread.stop()
                    thread = augmenteTRM(0.006)
                    thread.start()
                if event.value < -0.8 and event.value >= -1:
                    if(thread!=0):
                        thread.stop()
                    thread = augmenteTRM(0.002)
                    thread.start()

        if (good == 0):
            emo = pygame.image.load("icons/bad.png").convert_alpha()
            emo = pygame.transform.scale(emo, (50, 50))
            position_emo = emo.get_rect()
            position_emo.center = 490,50
        if (good ==2):
            emo = pygame.image.load("icons/good.png").convert_alpha()
            emo = pygame.transform.scale(emo, (50, 50))
            position_emo = emo.get_rect()
            position_emo.center = 490,50
        if (good == 3):
            emo = pygame.image.load("icons/love.png").convert_alpha()
            emo = pygame.transform.scale(emo, (50, 50))
            position_emo = emo.get_rect()
            position_emo.center = 490,50

            # if event.axis == 2:
            #     if event.value < -0.1 and event.value >= -1:
            #         #print(mon_joystick.get_axis(2))#accelerer
            #         tour = tour - mon_joystick.get_axis(2)* 60
            #         print(tour)
            #     elif event.value > 0.1 and event.value <= 1:
            #         if tour > 1060:
            #             tour = tour - mon_joystick.get_axis(2)* 60
            #         else:
            #             tour=1000
            #         print(tour)



    #Re-collage
    fenetre.blit(fond, (0,0))
    text2 = font.render("tr/min",1,(0,0,0))
    fenetre.blit(text2, (70, 390))
    text4 = font.render("km/h",1,(0,0,0))
    fenetre.blit(text4, (180, 390))
    fenetre.fill(Color("black"),(240,35,140,40))
    text5 = font.render("Score : "+str(score),1,(255,255,255))
    fenetre.blit(text5, (250, 45))
    vit = (TRM + rapport*1000 - 2000)/50
    text3 = font.render(str(vit),1,(255,255,255))
    fenetre.fill(Color("black"),(160,330,80,60))
    fenetre.blit(text3, (175, 350))
    fenetre.blit(perso, position_perso)
    fenetre.fill(Color("black"),(50,330,80,60))
    fenetre.blit(text, (65, 350))
    fenetre.blit(clid, position_clid)
    fenetre.blit(clig, position_clig)
    fenetre.blit(rap, position_rap)
    fenetre.blit(emo, position_emo)
    #Rafraichissement
    pygame.display.flip()
