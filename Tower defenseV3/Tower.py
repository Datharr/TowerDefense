from Collide import *
import random
class Tower:
    def __init__(self,x,y,arrow,path,vie,rect,type,range):
        self.x = x
        self.y = y
        self.size_x = 80
        self.size_y = 100
        self.range = range
        self.arrow = arrow
        self.attack = 100
        self.path = path
        self.vie = vie
        self.rect = rect
        self.type = type
        self.hitbox = Collide(self.x - (self.range - self.size_x) / 2, self.y - (self.range - self.size_y) / 2, self.range, self.range)  #Mettre une range
        self.addon = Collide(self.x-35, self.y-10 , 150, 150)
        self.targetable = []
        self.structure = 1
        self.further = None
        self.upgrade = {"Speed":None,"Attack":None,"Range":None}

    def upgrade_range(self,newrange):
        self.range = newrange
        self.hitbox = Collide(self.x - (newrange - self.size_x) / 2, self.y - (newrange - self.size_y) / 2, newrange, newrange)
        self.addon = Collide(self.x-35, self.y-10 , 150, 150)


    
    # def drawrect(self,hitbox):
    #     # return self.hitbox.pos_x,self.hitbox.pos_y,self.hitbox.size_x,self.hitbox.size_y
    #     return 60,50,20,80
