import pygame
import os
import random
import time
from Monsters import *
from Collide import *
from Effect import *
from Tower import *

def check_input_exit():
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                exit()

def loading_monsters(monster_list,nombre):          #générateur de monstre en fonction de "nombre"
    for a in range (nombre):
        monster_list.append(Monster(100,10,10,1820,240,0,0,0,0,0,random.randint(0, 5)))
        #random.randint(0, 5)
    return monster_list

def the_further(monster_list, far, far2): #calcul du monstre le plus loin en fonction du pathing far = le plus loin sur le chemin du haut / far2 = le plus loin sur le chemin du bas
    far = 0
    far2 = 0

    for a in range (len(monster_list)):
        if monster_list[a].path == 0:
            if monster_list[a].x <= monster_list[far].x:
                far = a
        
    for b in range (len(monster_list)):    
        if monster_list[b].path == 1:
            if monster_list[b].x <= monster_list[far2].x:
                far2 = b

    return far, far2

def display_text(win, text, positionX, positionY, size,R,G,B):    #Fonction texte             #fonction pour afficher du texte à l'écran
    font = pygame.font.SysFont("arial", size)                     #Police et taille
    font.set_bold(True)                                   
    text = font.render(text, True, (R, G, B), None)               #Couleur
    win.blit(text, (positionX, positionY))                        #Position du texte

def loading_wave(monster_list,wave_list):
    for monster_id in range (len(wave_list)):
        for a in range (wave_list[monster_id]):
            monster_list.append(Monster(100,10,10,1820,240,0,0,0,0,0,monster_id))
    
    return monster_list

def random_height():                        #fonction pour randomiser les valeurs y des monstres 
    random = random.randint(240, 320)
    return random

def load_effect(effect_list,x,y,path,variation,movemax,movement,caract):
    effect_list.append(Effect(x,y,path,variation,movemax,movement,caract))
    return effect_list

def path1(monster_list,a):                 #fonction pour faire le chemin de la carte
    if monster_list[a].path == 0:
            if monster_list[a].rect_pos == 0:
                monster_list[a].x -= monster_list[a].spd
                if monster_list[a].x <= random.randint(1306, 1374):
                    monster_list[a].rect_pos = 1
            if monster_list[a].rect_pos == 1:
                monster_list[a].y += 5
                if monster_list[a].y >= random.randint(363, 437):
                    monster_list[a].rect_pos = 2
            if monster_list[a].rect_pos == 2:
                monster_list[a].x -= monster_list[a].spd
                if monster_list[a].x <= random.randint(1004, 1167):
                    monster_list[a].rect_pos = 3
            if monster_list[a].rect_pos == 3:
                monster_list[a].y -= 5
                if monster_list[a].y <= random.randint(120, 220):
                    monster_list[a].rect_pos = 4
            if monster_list[a].rect_pos == 4:
                monster_list[a].x -= monster_list[a].spd
                if monster_list[a].x <= random.randint(665, 744):
                    monster_list[a].rect_pos = 5
            if monster_list[a].rect_pos == 5:
                monster_list[a].y += 5
                if monster_list[a].y >= random.randint(253, 335):
                    monster_list[a].rect_pos = 6 
            if monster_list[a].rect_pos == 6:
                monster_list[a].x -= monster_list[a].spd
                if monster_list[a].x <= random.randint(450, 538):
                    monster_list[a].rect_pos = 7
            if monster_list[a].rect_pos == 7:
                monster_list[a].y += 5
                if monster_list[a].y >= random.randint(480, 557):
                    monster_list[a].rect_pos = 8
            if monster_list[a].rect_pos == 8 or monster_list[a].rect_pos == 9:
                monster_list[a].x -= monster_list[a].spd
                if monster_list[a].x <= 0:
                    monster_list[a].rect_pos = 9
            return monster_list
    elif monster_list[a].path == 1:
        if monster_list[a].rect_pos == 0:
            monster_list[a].x -= monster_list[a].spd
            if monster_list[a].x <= 1760:
                monster_list[a].rect_pos = 1
        if monster_list[a].rect_pos == 1:
            monster_list[a].y += 5
            if monster_list[a].y >= 865:
                monster_list[a].rect_pos = 2
        if monster_list[a].rect_pos == 2:
            monster_list[a].x -= monster_list[a].spd
            if monster_list[a].x <= 1345:
                monster_list[a].rect_pos = 3
        if monster_list[a].rect_pos == 3:
            monster_list[a].y += 5
            if monster_list[a].y >= 985:
                monster_list[a].rect_pos = 4
        if monster_list[a].rect_pos == 4:
            monster_list[a].x -= monster_list[a].spd
            if monster_list[a].x <= 1125:
                monster_list[a].rect_pos = 5
        if monster_list[a].rect_pos == 5:
            monster_list[a].y -= 5
            if monster_list[a].y <= 834:
                monster_list[a].rect_pos = 6 
        if monster_list[a].rect_pos == 6:
            monster_list[a].x -= monster_list[a].spd
            if monster_list[a].x <= 1004:
                monster_list[a].rect_pos = 7
        if monster_list[a].rect_pos == 7:
            monster_list[a].y -= 5
            if monster_list[a].y <= 717:
                monster_list[a].rect_pos = 8
        if monster_list[a].rect_pos == 8:
            monster_list[a].x -= 10
            if monster_list[a].x <= 702:
                monster_list[a].rect_pos = 9
        if monster_list[a].rect_pos == 9:
            monster_list[a].y += 5
            if monster_list[a].y >= 870:
                monster_list[a].rect_pos = 10   
        if monster_list[a].rect_pos == 10:
            monster_list[a].x -= monster_list[a].spd
            if monster_list[a].x <= 268:
                monster_list[a].rect_pos = 11
        if monster_list[a].rect_pos == 11:
            monster_list[a].y -= 5
            if monster_list[a].y <= 531:
                monster_list[a].rect_pos = 12
        if monster_list[a].rect_pos == 12:
            monster_list[a].x -= monster_list[a].spd
            if monster_list[a].x <= -200:
                monster_list[a].rect_pos = 13




    return monster_list

def arrow_traj(monster_list, far, far2, projectile_list, a, data, arrow, effect_list): #codage des flèches
    print("a: " + str(a))
    print("building_list: " + str(len(building_list)))

    print("far: " + str(far))
    print("monster_list: " + str(len(monster_list)))
    if building_list[a].hitbox.check_collide(monster_list[far].hitbox) == True:  #voit si on est dans la range avec la méthode .check_collide de la class collide
        if building_list[a].path == 0 and projectile_list[a]["cd"] == 0:
            if projectile_list[a]["x"] < monster_list[far].x:
                projectile_list[a]["x"] += 15
                arrow = rotate_arrow("images/arrow.png",0)
            else: 
                projectile_list[a]["x"] -= 15
                arrow = rotate_arrow("images/arrow.png",-80)


            if projectile_list[a]["y"] < monster_list[far].y:
                projectile_list[a]["y"] += 15
            else: 
                projectile_list[a]["y"] -= 15

            if projectile_list[a]["x"] >= monster_list[far].x-10 and projectile_list[a]["x"] <= monster_list[far].x+10  :
                effect_list = load_effect(effect_list, monster_list[far].x, monster_list[far].y, "animation/blood/", 9, 30, 1, 2)
                monster_list.pop(far)
                projectile_list[a]["cd"] = projectile_list[a]["cdmax"]
                data["money"] += 5
                projectile_list[a]["x"] = projectile_list[a]["reset_x"]
                projectile_list[a]["y"] = projectile_list[a]["reset_y"]
        else : 
            projectile_list[a]["cd"] -= 1
            if projectile_list[a]["cd"] <= 0:
                projectile_list[a]["cd"] = 0
        
    
    #----------------------------
    if building_list[a].path == 1 and projectile_list[a]["cd"] == 0:
        if projectile_list[a]["x"] < monster_list[far2].x:
            projectile_list[a]["x"] += 15
            arrow = rotate_arrow("images/arrow.png",0)
        else: 
            projectile_list[a]["x"] -= 15
            arrow = rotate_arrow("images/arrow.png",-80)

        if projectile_list[a]["y"] < monster_list[far2].y:
            projectile_list[a]["y"] += 15
        else: 
            projectile_list[a]["y"] -= 15

        if projectile_list[a]["x"] >= monster_list[far2].x-10 and projectile_list[a]["x"] <= monster_list[far2].x+10  :
            monster_list.pop(far2)
            data["money"] += 5
            projectile_list[a]["x"] = projectile_list[a]["reset_x"]
            projectile_list[a]["y"] = projectile_list[a]["reset_y"]
    else : 
        projectile_list[a]["cd"] -= 1
        if projectile_list[a]["cd"] <= 0:
            projectile_list[a]["cd"] = 0


    return projectile_list,monster_list,data,arrow,effect_list

def build(monster_list,logo1_rect,building_list,projectile_list,State,data):   #cliquer sur le bouton en bas a gauche met en mode "construction"
    mouse_pos = pygame.mouse.get_pos()
    mouse_p = pygame.mouse.get_pressed()
    if data["money"] >= 50:
        if mouse_p[0] == True:
            if logo1_rect.collidepoint(mouse_pos):
                State = True
            return building_list,projectile_list,State


    return building_list,projectile_list,State

def cursor(State,building_list,data,effect_list): #fonction pour construire un batiment une fois en mode "construction"
    if State == True :
        win.blit(tower1,(mouse_pos))
        mouse_p = pygame.mouse.get_pressed()
        if mouse_p[0] == True:
            building_list.append(Tower(mouse_pos[0],mouse_pos[1],0,0,0,0))
            projectile_list.append({"x":mouse_pos[0],"y":mouse_pos[1],"reset_x":mouse_pos[0],"reset_y":mouse_pos[1],"cd":0,"cdmax":10})
            data["money"] -= 50
            State = False
            effect_list = load_effect(effect_list, mouse_pos[0], mouse_pos[1], "animation/build_effect/", 3, 32, 1, 1)
            if  building_list[-1].y >= 571:
                building_list[-1].path = 1
    return building_list,State,data,effect_list

def spd_button(actual_spd,spd_logo):
    mouse_pos = pygame.mouse.get_pos()
    mouse_p = pygame.mouse.get_pressed()

    if mouse_p[0] == True:
        if logo2_rect.collidepoint(mouse_pos):
            actual_spd += 20
            if actual_spd >= 80:
                actual_spd = 20
        if actual_spd == 20:
            spd_logo = pygame.image.load("images/x1.jpg").convert()
        elif actual_spd == 40:
            spd_logo = pygame.image.load("images/x2.jpg").convert()
        elif actual_spd == 60:
            spd_logo = pygame.image.load("images/x3.jpg").convert()
        spd_logo = pygame.transform.scale(spd_logo, (118, 104))

    return actual_spd,spd_logo


def movement_goblin(monster_list):    #fonction pour coder l'animation des monstres
    for a in range (len(monster_list)):
        monster_list[a].movement += 1

        if monster_list[a].movement > monster_list[a].movemax:
            monster_list[a].movement  = 1 

    return monster_list    

def rotate_arrow(image,angle):   #fonction pour tourner la flèche en fonction de l'angle qu'on lui donne
    arrow_base = pygame.image.load(image).convert_alpha()
    arrow_base = pygame.transform.scale(arrow_base, (40, 40))
    arrow = pygame.transform.rotate(arrow_base, angle)
    
    return arrow


if __name__ == "__main__":  #programme main 

    pygame.init()
    far,far2,distance = 0,0,0
    clock = pygame.time.Clock()
    win = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
    State = False

    data = {"pv":100,"money":1000}
    monster_list = []

    building_list = [
        Tower(1412,100,0,0,0,0)
    ]

    projectile_list = [{"x":1412,"y":100,"reset_x":1412,"reset_y":100,"cd":0,"cdmax":10}

    ]

    wave_list = [2,3,4,0,7,0]
    effect_list = []
    actual_spd = 20
    load_effect(effect_list, 0, 70, "animation/coin/", 2, 12, 1, 4)
    # monster_list = loading_monsters(monster_list,50)
    monster_list = loading_wave(monster_list,wave_list)
    logo1_rect = pygame.draw.rect(win, (0, 200, 0), (0,  962, 118, 104))
    logo2_rect = pygame.draw.rect(win, (0, 200, 0), (0,  876, 118, 104))
    
    for a in range (len(monster_list)):
        monster_list[a].path = random.randint(0, 1)
        if monster_list[a].path == 0:
            monster_list[a].y = random.randint(240, 320)
            monster_list[a].x = random.randint(1750, 3000)
        if monster_list[a].path == 1:
            monster_list[a].y = random.randint(740, 760) 
            monster_list[a].x =  random.randint(1750, 3000)   
        monster_list[a].movement = random.randint(1, 10)

    
    lvl1 = pygame.image.load("images/map.jpg").convert()
    lvl1 = pygame.transform.scale(lvl1, (1920, 1080))
    rect = pygame.image.load("images/rect.png").convert()
    rect = pygame.transform.scale(rect, (40, 40))
    tower1 = pygame.image.load("images/tower1.png").convert_alpha()
    tower1 = pygame.transform.scale(tower1, (80, 100))
    arrow = rotate_arrow("images/arrow.png",0)
    rect_blue = pygame.image.load("images/rect_blue.png").convert_alpha()
    rect_blue = pygame.transform.scale(rect_blue, (40, 40))
    build_logo = pygame.image.load("images/logotest.jpg").convert()
    build_logo = pygame.transform.scale(build_logo, (118, 104))
    spd_logo = pygame.image.load("images/x1.jpg").convert()
    spd_logo = pygame.transform.scale(spd_logo, (118, 104))
    # build_logo = pygame.transform.scale(build_logo, (40, 40))
    while True:                                                       #boucle de jeu
        clock.tick(actual_spd)                                                #nombre de tour de boucle par seconde (FPS)
        win.blit(lvl1, (0, 0))
        win.blit(build_logo, (-5,980))
        win.blit(spd_logo, (-5,876))
        far, far2 = the_further(monster_list, far, far2)                #utilisation de la fonction calculant le plus loin et recuperation des valeurs far et far2
        mouse_pos = pygame.mouse.get_pos()                            #recuperation de la pos de la souris en tuple(x,y)
        mouse_p = pygame.mouse.get_pressed()                          #recuperation si le clique de la souris à été pressé soit True soit False
        building_list,State,data,effect_list = cursor(State,building_list,data,effect_list)
        building_list,projectile_list,State = build(monster_list,logo1_rect,building_list,projectile_list,State,data)
        monster_list = movement_goblin(monster_list)
        actual_spd,spd_logo = spd_button(actual_spd,spd_logo)
        display_text(win,str(data["money"]),100, 100, 50,0,0,255)                      #affichage de l'argent avec (fenêtre,texte,x,y,taille,(couleur RGB))
        for a in range (len(building_list)):
            pygame.draw.rect(win, [0, 200, 0], [building_list[a].hitbox.pos_x,building_list[a].hitbox.pos_y,building_list[a].hitbox.size_x,building_list[a].hitbox.size_y])
            #enlever le # permet de voir les hitbox
            win.blit(tower1, (building_list[a].x, building_list[a].y))

        for a in range (len(projectile_list)):            #affichage de toutes les flèches
            projectile_list,monster_list,data,arrow,effect_list = arrow_traj(monster_list,far,far2,projectile_list,a,data,arrow,effect_list) 
            win.blit(arrow, (projectile_list[a]["x"], projectile_list[a]["y"]))
        
        len_effect = len(effect_list)
        a = 0
        while a < len_effect:
            if effect_list[a].caract == 1:
                effect_show = pygame.image.load(effect_list[a].path + str(effect_list[a].actual_variation) + "/1_" + str(effect_list[a].movement) + ".png").convert_alpha()
                effect_show = pygame.transform.scale(effect_show, (200, 200))
                win.blit(effect_show, (effect_list[a].x-60,effect_list[a].y-50))
            elif effect_list[a].caract == 2:
                effect_show = pygame.image.load(effect_list[a].path + str(effect_list[a].actual_variation) + "/" + str(effect_list[a].movement) + ".png").convert_alpha()
                effect_show = pygame.transform.scale(effect_show, (64, 64))
                win.blit(effect_show, (effect_list[a].x-40,effect_list[a].y))

            elif effect_list[a].caract == 4:
                effect_show = pygame.image.load(effect_list[a].path + str(effect_list[a].actual_variation) + "/" + str(effect_list[a].movement) + ".png").convert_alpha()  
                win.blit(effect_show, (effect_list[a].x,effect_list[a].y))

            effect_list[a].movement += 1
            if effect_list[a].movement >= effect_list[a].movemax:
                effect_list[a].movement = 1
                if effect_list[a].caract != 4:
                    effect_list.pop(a)   
                    len_effect = len(effect_list)

            a += 1 
                    
        
        for a in range (len(monster_list)):            #affichage des carrés bleues pour les monstres les plus loins else un simple sprite de monstre 
            if far == a or far2 == a:
                # pygame.draw.rect(win, [255, 0, 0], [monster_list[a].hitbox.pos_x,monster_list[a].hitbox.pos_y,monster_list[a].hitbox.size_x,monster_list[a].hitbox.size_y])
                #enlever le # permet de voir les hitbox
                win.blit(rect_blue, (monster_list[a].x, monster_list[a].y))
                monster_list = path1(monster_list,a)
                monster_list[a].hitbox.update_rect(monster_list[a].x,monster_list[a].y)

            else:
                rect2 = pygame.image.load(monster_list[a].pathmove + str(monster_list[a].movement) + ".png").convert_alpha()
                rect2 = pygame.transform.scale(rect2, (monster_list[a].xsize, monster_list[a].ysize))
                monster_list = path1(monster_list,a)
                # pygame.draw.rect(win, [0, 0, 255], [monster_list[a].hitbox.pos_x,monster_list[a].hitbox.pos_y,monster_list[a].hitbox.size_x,monster_list[a].hitbox.size_y])
                #enlever le # permet de voir les hitbox
                win.blit(rect2, (monster_list[a].x, monster_list[a].y))
                monster_list[a].hitbox.update_rect(monster_list[a].x,monster_list[a].y)
        #-------------------------------------------------------
       
        pygame.display.flip()       #actualisation de l'écran 
        check_input_exit()                #voit si on veut quitter le jeu avec ECHAP


