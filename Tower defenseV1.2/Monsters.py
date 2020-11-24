from pygame.rect import Rect
from Collide import *
import pygame


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

        if self.type == -1:
            self.pathmove = "monsters/rect/run/run"   
            self.movemax = 1               
            self.xsize = 48
            self.ysize = 48
        if self.type == 0:
            self.pathmove = "monsters/goblin/run/run"
            self.movemax = 10
            self.xsize = 48
            self.ysize = 72
        if self.type == 1:
            self.pathmove = "monsters/knight/run/run"
            self.spd -= 4
            self.movemax = 12
            self.xsize = 66
            self.ysize = 82
        if self.type == 2:
            self.pathmove = "monsters/orc/run/run"
            self.movemax = 8
            self.xsize = 58
            self.ysize = 36
        if self.type == 3:
            self.pathmove = "monsters/roguelike/run/run"
            self.movemax = 6
            self.xsize = 34
            self.ysize = 40
        if self.type == 4:
            self.pathmove = "monsters/minotaur/run/run"
            self.spd -= 4
            self.movemax = 16
            self.xsize = 104
            self.ysize = 82
        if self.type == 5:
            self.pathmove = "monsters/dwarf/run/run"
            self.movemax = 8
            self.xsize = 42
            self.ysize = 36
