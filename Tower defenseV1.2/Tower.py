from Collide import *

class Tower:
    def __init__(self,x,y,arrow,path,vie,rect):
        self.x = x
        self.y = y
        self.size_x = 80
        self.size_y = 100
        self.range = 300
        self.arrow = arrow
        self.path = path
        self.vie = vie
        self.rect = rect
        self.hitbox = Collide(self.x - (self.range - self.size_x) / 2, self.y - (self.range - self.size_y) / 2, self.range, self.range)  #Mettre une range
        self.targetable = []
        self.further = None

    
    # def drawrect(self,hitbox):
    #     # return self.hitbox.pos_x,self.hitbox.pos_y,self.hitbox.size_x,self.hitbox.size_y
    #     return 60,50,20,80
