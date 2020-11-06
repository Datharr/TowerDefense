from pygame.rect import Rect
from Collide import *
import random



class Effect:
    def __init__(self,x,y,path,variation,movemax,movement,caract):
        self.x = x
        self.y = y
        self.path = path
        self.variation = variation
        self.actual_variation = random.randint(1,self.variation)
        self.movemax = movemax
        self.movement = movement     
        self.caract = caract 
