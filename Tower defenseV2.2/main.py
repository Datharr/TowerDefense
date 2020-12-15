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

def the_further(monster_list, building_list): #calcul du monstre le plus loin en fonction du pathing far = le plus loin sur le chemin du haut / far2 = le plus loin sur le chemin du bas



    # recupere les index des monstres qui sont dans la range de chacune des tours
    for b in range (len(building_list)):
        building_list[b].targetable = []

    for b in range (len(building_list)):
        for m in range (len(monster_list)):
            if building_list[b].hitbox.check_collide(monster_list[m].hitbox) == True:
                building_list[b].targetable.append(m)
    
  
    # trouve le plus loin parmi ceux dans la range

    for b in range (len(building_list)):
        for m in (building_list[b].targetable):

            if building_list[b].further == None:
                building_list[b].further = monster_list[m]

            if building_list[b].further.x <= monster_list[m].x:
                building_list[b].further = monster_list[m]

        if len(building_list[b].targetable) == 0:
            building_list[b].further = None    

            

    #     if monster_list[a].path == 0:
    #         if monster_list[a].x <= monster_list[far].x:
    #             far = a
        
    # for b in range (len(monster_list)):    
    #     if monster_list[b].path == 1:
    #         if monster_list[b].x <= monster_list[far2].x:
    #             far2 = b

    return building_list

def display_text(win, text, positionX, positionY, size,R,G,B):    #Fonction texte             #fonction pour afficher du texte à l'écran
    font = pygame.font.SysFont("arial", size)                     #Police et taille
    font.set_bold(True)                                   
    text = font.render(text, True, (R, G, B), None)               #Couleur
    win.blit(text, (positionX, positionY))                        #Position du texte

def loading_wave(monster_list,wave_list):
    for monster_id in range (len(wave_list)):
        for a in range (wave_list[monster_id]):
            monster_list.append(Monster(100,10,10,1820,240,0,0,0,0,0,monster_id))
    
    for a in range (len(monster_list)):
        monster_list[a].path = random.randint(0, 1)
        if monster_list[a].path == 0:
            monster_list[a].y = random.randint(223, 300)
            monster_list[a].x = random.randint(2000, 3500)
        if monster_list[a].path == 1:
            monster_list[a].y = random.randint(640, 755) 
            monster_list[a].x =  random.randint(2000, 3500)   
        monster_list[a].movement = random.randint(1, 5)
    
    return monster_list

def load_effect(effect_list,x,y,path,variation,movemax,movement,caract):
    effect_list.append(Effect(x,y,path,variation,movemax,movement,caract))
    return effect_list

def path1(monster_list,a):                 #fonction pour faire le chemin de la carte
    if monster_list[a].path == 0:
            if monster_list[a].rect_pos == 0:
                monster_list[a].x -= monster_list[a].spd
                if monster_list[a].x <= monster_list[a].livre[0]:
                    monster_list[a].rect_pos = 1
            if monster_list[a].rect_pos == 1:
                monster_list[a].y += monster_list[a].spd
                if monster_list[a].y >= monster_list[a].livre[1]:
                    monster_list[a].rect_pos = 2
            if monster_list[a].rect_pos == 2:
                monster_list[a].x -= monster_list[a].spd
                if monster_list[a].x <= monster_list[a].livre[2]:
                    monster_list[a].rect_pos = 3
            if monster_list[a].rect_pos == 3:
                monster_list[a].y -= monster_list[a].spd
                if monster_list[a].y <= monster_list[a].livre[3]:
                    monster_list[a].rect_pos = 4
            if monster_list[a].rect_pos == 4:
                monster_list[a].x -= monster_list[a].spd
                if monster_list[a].x <= monster_list[a].livre[4]:
                    monster_list[a].rect_pos = 5
            if monster_list[a].rect_pos == 5:
                monster_list[a].y += monster_list[a].spd
                if monster_list[a].y >= monster_list[a].livre[5]:
                    monster_list[a].rect_pos = 6 
            if monster_list[a].rect_pos == 6:
                monster_list[a].x -= monster_list[a].spd
                if monster_list[a].x <= monster_list[a].livre[6]:
                    monster_list[a].rect_pos = 7
            if monster_list[a].rect_pos == 7:
                monster_list[a].y += monster_list[a].spd
                if monster_list[a].y >= monster_list[a].livre[7]:
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

def arrow_traj(monster_list,building_list, far, far2, projectile_list, a, data, arrow, effect_list): #codage des flèches


    # if building_list[a].hitbox.check_collide(monster_list[building_list[a].further].hitbox) == True:
    if building_list[a].type == 0:
        if building_list[a].further != None:
            if projectile_list[a]["cd"] == 0:
                if projectile_list[a]["x"] < building_list[a].further.x:
                    projectile_list[a]["x"] += 15
                    arrow = rotate_arrow("images/arrow.png",180)
                else: 
                    projectile_list[a]["x"] -= 15
                    arrow = rotate_arrow("images/arrow.png",-80)


                if projectile_list[a]["y"] < building_list[a].further.y:
                    projectile_list[a]["y"] += 15
                else: 
                    projectile_list[a]["y"] -= 15

                if projectile_list[a]["x"] >= building_list[a].further.x-10 and projectile_list[a]["x"] <= building_list[a].further.x+10  :
                    effect_list = load_effect(effect_list, building_list[a].further.x, building_list[a].further.y, "animation/blood/", 9, 30, 1, 2)
                    if building_list[a].further in monster_list:
                        building_list[a].further.pv -= building_list[a].attack
                        if building_list[a].further.pv <= 0 :   
                            monster_list.pop(monster_list.index(building_list[a].further))
                    projectile_list[a]["cd"] = projectile_list[a]["cdmax"]
                    data["money"] += 5
                    projectile_list[a]["x"] = projectile_list[a]["reset_x"]
                    projectile_list[a]["y"] = projectile_list[a]["reset_y"]
            else : 
                projectile_list[a]["cd"] -= 1
                if projectile_list[a]["cd"] <= 0:
                    projectile_list[a]["cd"] = 0

    elif building_list[a].type == 1:
        for c in range (len(monster_list)):
            if c in building_list[a].targetable:
                monster_list[c].spd = monster_list[c].spdbase/2
            else: 
                monster_list[c].spd = monster_list[c].spdbase







    return projectile_list,monster_list,building_list,data,arrow,effect_list

def build(monster_list,logo1_rect,logo3_rect,logo4_rect,building_list,projectile_list,State,data):   #cliquer sur le bouton en bas a gauche met en mode "construction"
    mouse_pos = pygame.mouse.get_pos()
    mouse_p = pygame.mouse.get_pressed()
    if data["money"] >= 100:
        if mouse_p[0] == True:
            if logo1_rect.collidepoint(mouse_pos):
                State = 1
            elif logo3_rect.collidepoint(mouse_pos) and data["money"] >= 250:
                State = 2
            elif logo4_rect.collidepoint(mouse_pos) and data["money"] >= 300:
                State = 3
            return building_list,projectile_list,State


    return building_list,projectile_list,State

def cursor(State,building_list,data,effect_list): #fonction pour construire un batiment une fois en mode "construction"
    if State == 1 :
        win.blit(tower1,(mouse_pos))
        mouse_p = pygame.mouse.get_pressed()
        if mouse_p[0] == True:
            building_list.append(Tower(mouse_pos[0],mouse_pos[1],0,0,0,0,0,500))
            projectile_list.append({"x":mouse_pos[0],"y":mouse_pos[1],"reset_x":mouse_pos[0],"reset_y":mouse_pos[1],"cd":0,"cdmax":10})
            data["money"] -= 100
            State = 0
            effect_list = load_effect(effect_list, mouse_pos[0], mouse_pos[1], "animation/build_effect/", 3, 32, 1, 1)
            if  building_list[-1].y >= 571:
                building_list[-1].path = 1
    elif State == 2 :
        win.blit(wizard1,(mouse_pos))
        mouse_p = pygame.mouse.get_pressed()
        if mouse_p[0] == True:
            building_list.append(Tower(mouse_pos[0],mouse_pos[1],0,0,0,0,1,350))
            projectile_list.append({"x":mouse_pos[0],"y":mouse_pos[1],"reset_x":mouse_pos[0],"reset_y":mouse_pos[1],"cd":0,"cdmax":10})
            data["money"] -= 250
            State = 0
            effect_list = load_effect(effect_list, mouse_pos[0], mouse_pos[1], "animation/build_effect/", 3, 32, 1, 1)
            if  building_list[-1].y >= 571:
                building_list[-1].path = 1
    elif State == 3:
        win.blit(wizard3,(mouse_pos))
        mouse_p = pygame.mouse.get_pressed()
        if mouse_p[0] == True:
            building_list.append(Tower(mouse_pos[0],mouse_pos[1],0,0,0,0,2,350))
            projectile_list.append({"x":mouse_pos[0],"y":mouse_pos[1],"reset_x":mouse_pos[0],"reset_y":mouse_pos[1],"cd":0,"cdmax":10})
            data["money"] -= 300
            State = 0
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

def open_portal(wave_state,b):
    
    if wave_state == 0:
        portal = pygame.image.load("animation/portal/open/open"+ str(b) +".png").convert_alpha()

        if b >= 8:
            b = 1
            wave_state = 1
    if wave_state == 1:
        portal = pygame.image.load("animation/portal/spawn/spawn"+ str(b) +".png").convert_alpha()
        rect_portal = pygame.Rect(1877,  240, 100, 100)
        rect_portal2 = pygame.Rect(1877,  663, 100, 100)
        mouse_pos = pygame.mouse.get_pos()
        mouse_p = pygame.mouse.get_pressed()

        if b >= 8:
            b = 1
        if mouse_p[0] == True:
            if rect_portal.collidepoint(mouse_pos) or rect_portal2.collidepoint(mouse_pos):
                wave_state = 2
                b = 1
        
    b += 1
    if wave_state == 2:
        portal = pygame.image.load("animation/portal/close/close"+ str(b) +".png").convert_alpha()    
        if b >= 6:
            b = 1
            wave_state = 3
    portal = pygame.transform.scale(portal, (58, 70))
    win.blit(portal, (1880,260))
    win.blit(portal, (1880,680))
    
    return wave_state,b

def wave_end(monster_list,wave_state,wave_list,wave_number):

    if wave_list[wave_number] == wave_list[0] and wave_state == 3 and wave_number == 0:
        wave_number = 1

    if len(monster_list) == 0 and wave_list[wave_number] != wave_list[0] and wave_state > 3 :
        wave_state = 0

    return wave_state,wave_number

def shop(building_list,data,a,mouse_pos,mouse_p,circle_shop,item1,item2,item3):

    # pygame.draw.rect(win, (0, 200, 0), (building_list[a].x-35,building_list[a].y-10, 150, 150))
    if building_list[a].type == 0:
        if building_list[a].addon.check_mouse(mouse_pos):
            win.blit(circle_shop, (building_list[a].x-23,building_list[a].y+21))
            
            if building_list[a].upgrade["Attack"] == None and building_list[a].upgrade["Speed"] == None:
                win.blit(item1, (building_list[a].x-15,building_list[a].y+90))
                rect_topleft = pygame.Rect(building_list[a].x-15,  building_list[a].y+90, 24, 24)
                if mouse_p[0] == True and data["money"] >= 100:
                    if rect_topleft.collidepoint(mouse_pos):
                        data["money"] -= 100  
                        building_list[a].structure = 4
                        building_list[a].upgrade["Attack"] = 1
                        building_list[a].attack = 250

            if building_list[a].upgrade["Speed"] == None and building_list[a].upgrade["Attack"] == None:
                win.blit(item2, (building_list[a].x-15,building_list[a].y+30))   
                rect_botleft = pygame.Rect(building_list[a].x-15,  building_list[a].y+30, 24, 24) 
                if mouse_p[0] == True and data["money"] >= 100:
                    if rect_botleft.collidepoint(mouse_pos):
                        data["money"] -= 100
                        building_list[a].structure = 3
                        building_list[a].upgrade["Speed"] = 1
                        projectile_list[a]["cdmax"] = 4

    
    return building_list,data   

def calculate_points_projectile(src, dest, count):
    points = []
    dX = dest[0] - src[0]
    dY = dest[1] - src[1]
    interval_X = dX / (count + 1)
    interval_Y = dY / (count + 1)
    for i in range(count):
        points.append((src[0] + interval_X * i, src[1] + interval_Y * i))
    return points

def show_pv(monster_list,a,barre_list):
    if monster_list[a].pv != monster_list[a].pvmax:
        if  monster_list[a].pv > 90/100* monster_list[a].pvmax:
            win.blit(barre_list[8],(monster_list[a].x-15,monster_list[a].y-10))
            
        elif  monster_list[a].pv > 80/100* monster_list[a].pvmax:
            win.blit(barre_list[7],(monster_list[a].x-15,monster_list[a].y-10))

        elif  monster_list[a].pv > 70/100* monster_list[a].pvmax:
            win.blit(barre_list[6],(monster_list[a].x-15,monster_list[a].y-10))

        elif  monster_list[a].pv > 60/100* monster_list[a].pvmax:
            win.blit(barre_list[5],(monster_list[a].x-15,monster_list[a].y-10))

        elif  monster_list[a].pv > 50/100* monster_list[a].pvmax:
            win.blit(barre_list[4],(monster_list[a].x-15,monster_list[a].y-10))

        elif monster_list[a].pv > 40/100*monster_list[a].pvmax:
            win.blit(barre_list[3],(monster_list[a].x-15,monster_list[a].y-10))

        elif  monster_list[a].pv > 30/100* monster_list[a].pvmax:
            win.blit(barre_list[2],(monster_list[a].x-15,monster_list[a].y-10))
        
        elif  monster_list[a].pv > 20/100* monster_list[a].pvmax:
            win.blit(barre_list[1],(monster_list[a].x-15,monster_list[a].y-10))
        
        elif  monster_list[a].pv > 10/100*monster_list[a].pvmax:
            win.blit(barre_list[0],(monster_list[a].x-15,monster_list[a].y-10))

def hud_load_barre():



    barre1 = pygame.image.load("images/health_bar/Health_bar/barre10.png").convert_alpha()
    barre2 = pygame.image.load("images/health_bar/Health_bar/barre20.png").convert_alpha()
    barre3 = pygame.image.load("images/health_bar/Health_bar/barre30.png").convert_alpha()
    barre4 = pygame.image.load("images/health_bar/Health_bar/barre40.png").convert_alpha()
    barre5 = pygame.image.load("images/health_bar/Health_bar/barre50.png").convert_alpha()
    barre6 = pygame.image.load("images/health_bar/Health_bar/barre60.png").convert_alpha()
    barre7 = pygame.image.load("images/health_bar/Health_bar/barre70.png").convert_alpha()
    barre8 = pygame.image.load("images/health_bar/Health_bar/barre80.png").convert_alpha()
    barre9 = pygame.image.load("images/health_bar/Health_bar/barre90.png").convert_alpha()
    barre_list = [barre1,barre2,barre3,barre4,barre5,barre6,barre7,barre8,barre9]
    for a in range (0,len(barre_list)):
        barre_list[a] = pygame.transform.scale(barre_list[a], (45, 16))    
    return barre_list

def hud_load_item():
    item1 = pygame.image.load("images/items/Item__03.png").convert_alpha()
    item1 = pygame.transform.scale(item1, (24, 24))
    item2 = pygame.image.load("images/items/Item__18.png").convert_alpha()
    item2 = pygame.transform.scale(item2, (24, 24))
    item3 = pygame.image.load("images/items/Item__25.png").convert_alpha()
    item3 = pygame.transform.scale(item3, (24, 24))

    return item1,item2,item3

def hud_load_tower():
    tower1 = pygame.image.load("images/tower1.png").convert_alpha()
    tower1 = pygame.transform.scale(tower1, (80, 100))
    tower2 = pygame.image.load("images/tower2.png").convert_alpha()
    tower2 = pygame.transform.scale(tower2, (80, 100))
    tower3 = pygame.image.load("images/tower3.png").convert_alpha()
    tower3 = pygame.transform.scale(tower3, (80, 100))   
    tower4 = pygame.image.load("images/tower4.png").convert_alpha()
    tower4 = pygame.transform.scale(tower4, (80, 100))

    return tower1,tower2,tower3,tower4

def hud_load_wizard_tower():
    wizard1 = pygame.image.load("images/wizard1.png").convert_alpha()
    wizard1 = pygame.transform.scale(wizard1, (80, 100))
    wizard2 = pygame.image.load("images/wizard2.png").convert_alpha()
    wizard2 = pygame.transform.scale(wizard2, (80, 100))
    wizard3 = pygame.image.load("images/wizard3.png").convert_alpha()
    wizard3 = pygame.transform.scale(wizard3, (80, 100))

    return wizard1,wizard2,wizard3

def hud_load_hud():
    circle_shop = pygame.image.load("images/build_logo.png").convert_alpha()
    circle_shop = pygame.transform.scale(circle_shop, (115, 103))
    lvl1 = pygame.image.load("images/map.jpg").convert()
    lvl1 = pygame.transform.scale(lvl1, (1920, 1080))
    build_logo = pygame.image.load("images/logotest.jpg").convert()
    build_logo = pygame.transform.scale(build_logo, (118, 104))
    wizard_logo =  pygame.image.load("images/logo_wizard.jpg").convert()
    wizard_logo = pygame.transform.scale(wizard_logo, (118, 104))
    lava_logo = pygame.image.load("images/logolava.jpg").convert()
    lava_logo = pygame.transform.scale(lava_logo, (118, 104))
    spd_logo = pygame.image.load("images/x1.jpg").convert()
    spd_logo = pygame.transform.scale(spd_logo, (118, 104))
    rect_blue = pygame.image.load("images/rect_blue.png").convert_alpha()
    rect_blue = pygame.transform.scale(rect_blue, (40, 40))

    return circle_shop,lvl1,build_logo,wizard_logo,spd_logo,lava_logo,rect_blue

def hud_load_everything():

    circle_shop,lvl1,build_logo,wizard_logo,spd_logo,lava_logo,rect_blue = hud_load_hud()
    wizard1,wizard2,wizard3 = hud_load_wizard_tower()
    tower1,tower2,tower3,tower4 = hud_load_tower()        
    barre_list = hud_load_barre()
    item1,item2,item3 = hud_load_item()

    return circle_shop,lvl1,build_logo,wizard_logo,spd_logo,lava_logo,wizard1,wizard2,wizard3,tower1,tower2,tower3,tower4,barre_list,item1,item2,item3,rect_blue

if __name__ == "__main__":  #programme main 

    pygame.init()
    far,far2,distance = 0,0,0
    clock = pygame.time.Clock()
    win = pygame.display.set_mode((1920, 1080), pygame.FULLSCREEN)
    State = 0
    wave_state = 0
    b = 1

    data = {"pv":100,"money":1000}
    
    monster_list = []

    building_list = [
        Tower(1412,100,0,0,0,0,0,500)
    ]

    projectile_list = [{"x":1412,"y":100,"reset_x":1412,"reset_y":100,"cd":0,"cdmax":10}

    ]

    wave_list = [[0,0,0,0,0,0],[10,0,10,0,0,0],[1,10,0,1,1,0],[2,15,2,1,2,0]]
    actual_wave = wave_list[0]
    wave_number = 0
    effect_list = []
    actual_spd = 20
    load_effect(effect_list, 0, 70, "animation/coin/", 2, 12, 1, 4)
    monster_list = loading_wave(monster_list,wave_list[0])
    logo1_rect = pygame.draw.rect(win, (0, 200, 0), (0,  962, 118, 104))
    logo2_rect = pygame.draw.rect(win, (0, 200, 0), (0,  876, 118, 104))
    logo3_rect = pygame.draw.rect(win, (0, 200, 0), (113,  978, 118, 104))
    logo4_rect = pygame.draw.rect(win, (0, 200, 0), (231,  978, 118, 104))
    
    
    
    for a in range (len(monster_list)):
        monster_list[a].path = random.randint(0, 1)
        if monster_list[a].path == 0:
            monster_list[a].y = random.randint(223, 300)
            monster_list[a].x = random.randint(1750, 3000)
        if monster_list[a].path == 1:
            monster_list[a].y = random.randint(640, 755) 
            monster_list[a].x =  random.randint(1750, 3000)   
        monster_list[a].movement = random.randint(1, 10)


    circle_shop,lvl1,build_logo,wizard_logo,spd_logo,lava_logo,wizard1,wizard2,wizard3,tower1,tower2,tower3,tower4,barre_list,item1,item2,item3,rect_blue = hud_load_everything()
    arrow = rotate_arrow("images/arrow.png",0)


    # build_logo = pygame.transform.scale(build_logo, (40, 40))
    while True:                                                       #boucle de jeu
        clock.tick(actual_spd)                                                #nombre de tour de boucle par seconde (FPS)
        win.blit(lvl1, (0, 0))
        win.blit(build_logo, (-5,980))
        win.blit(wizard_logo, (113,978))
        win.blit(lava_logo, (231,978))
        win.blit(spd_logo, (-5,876))
        building_list = the_further(monster_list, building_list)                #utilisation de la fonction calculant le plus loin et recuperation des valeurs far et far2
        mouse_pos = pygame.mouse.get_pos()                            #recuperation de la pos de la souris en tuple(x,y)
        mouse_p = pygame.mouse.get_pressed()                          #recuperation si le clique de la souris à été pressé soit True soit False
        building_list,State,data,effect_list = cursor(State,building_list,data,effect_list)
        building_list,projectile_list,State = build(monster_list,logo1_rect,logo3_rect,logo4_rect,building_list,projectile_list,State,data)
        monster_list = movement_goblin(monster_list)
        actual_spd,spd_logo = spd_button(actual_spd,spd_logo)
        display_text(win,str(data["money"]),100, 100, 50,0,0,255)                      #affichage de l'argent avec (fenêtre,texte,x,y,taille,(couleur RGB))


        wave_state,wave_number = wave_end(monster_list,wave_state,wave_list,wave_number)

        if wave_state < 3:
            wave_state,b = open_portal(wave_state,b)
        elif wave_state == 3 : 
            monster_list = loading_wave(monster_list,wave_list[wave_number])
            wave_state = 4
            wave_number += 1


        for a in range (len(building_list)):
            pygame.draw.rect(win, [255, 0, 0], [building_list[a].hitbox.pos_x,building_list[a].hitbox.pos_y,building_list[a].hitbox.size_x,building_list[a].hitbox.size_y], 4)
            building_list,data = shop(building_list,data,a,mouse_pos,mouse_p,circle_shop,item1,item2,item3)
            #enlever le # permet de voir les hitbox
            if building_list[a].type == 0:
                if building_list[a].structure == 1:
                    win.blit(tower2, (building_list[a].x, building_list[a].y))
                if building_list[a].structure == 3:
                    win.blit(tower3, (building_list[a].x, building_list[a].y))
                if building_list[a].structure == 4:
                    win.blit(tower4, (building_list[a].x, building_list[a].y))
            if building_list[a].type == 1:
                win.blit(wizard1, (building_list[a].x, building_list[a].y))
            if building_list[a].type == 2:
                win.blit(wizard3, (building_list[a].x, building_list[a].y))                


        for a in range (len(projectile_list)):            #affichage de toutes les flèches
            projectile_list,monster_list,building_list,data,arrow,effect_list = arrow_traj(monster_list,building_list,far,far2,projectile_list,a,data,arrow,effect_list) 
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
                    
        
        for a in range (len(monster_list)):         
            show_pv(monster_list,a,barre_list)
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


