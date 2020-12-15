from pygame.rect import Rect
from Collide import *
import pygame
import random


class Monster:
    def __init__(self,pv,ad,spd,x,y,path,rect_pos,movement,xsize,ysize,typem):
        self.pv = pv
        self.ad = ad
        self.spd = spd
        self.x = x
        self.y = y
        self.path = path
        self.rect_pos = rect_pos
        self.movement = movement
        self.hitbox = Collide(self.x-50, self.y, 40, 73) #Mettre une range
        self.type = typem

        if self.path == 0:
            self.livre = [random.randint(1301, 1365),random.randint(373, 429),random.randint(1104, 1167)
                    ,random.randint(120, 200),random.randint(673, 737),random.randint(235, 329),random.randint(450, 535),
                    random.randint(480, 555)]

        if self.type == -1:
            self.pathmove = "monsters/rect/run/run"   
            self.movemax = 1               
            self.xsize = 48
            self.ysize = 48
        if self.type == 0:
            self.pathmove = "monsters/goblin/run/run"
            self.pv = 100
            self.movemax = 10
            self.xsize = 24
            self.ysize = 36
            self.spd -= 3
        if self.type == 1:
            self.pathmove = "monsters/knight/run/run"
            self.pv = 400
            self.movemax = 12
            self.xsize = 66
            self.ysize = 82
            self.spd -= 7
        if self.type == 2:
            self.pathmove = "monsters/orc/run/run"
            self.pv = 150
            self.movemax = 8
            self.xsize = 58
            self.ysize = 36
            self.spd -= 5
        if self.type == 3:
            self.pathmove = "monsters/roguelike/run/run"
            self.pv = 120
            self.movemax = 6
            self.xsize = 34
            self.ysize = 40
            self.spd -= 7
        if self.type == 4:
            self.pathmove = "monsters/minotaur/run/run"
            self.pv = 500
            self.movemax = 16
            self.xsize = 104
            self.ysize = 82
            self.spd -= 7
        if self.type == 5:
            self.pathmove = "monsters/dwarf/run/run"
            self.pv = 200
            self.movemax = 8
            self.xsize = 42
            self.ysize = 36
            self.spd -= 6
        if self.type == 6:
            self.pathmove = "monsters/gladiator/run/run"
            self.pv = 220
            self.movemax = 8
            self.xsize = 42
            self.ysize = 44
            self.spd -= 6
        if self.type == 7:
            self.pathmove = "monsters/imp/run/run"
            self.pv = 100
            self.movemax = 8
            self.xsize = 20
            self.ysize = 18
    
        self.pvmax = self.pv
        self.spdbase = self.spd