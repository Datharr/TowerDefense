from collide import * 

class tower:
    def __init__(self,x,y,arrow,path,vie,rect):
        self.x = x
        self.y = y
        self.arrow = arrow
        self.path = path
        self.vie = vie
        self.rect = rect
        self.hitbox = collide(self.x-150, self.y, 300, 300)  #Mettre une range
    
    # def drawrect(self,hitbox):
    #     # return self.hitbox.pos_x,self.hitbox.pos_y,self.hitbox.size_x,self.hitbox.size_y
    #     return 60,50,20,80
