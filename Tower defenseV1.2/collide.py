from pygame.rect import Rect

class collide: #creation d'un carré hitbox 
    def __init__(self, pos_x, pos_y, size_x, size_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y
        self.hitbox_rect = Rect(pos_x, pos_y, size_x, size_y)

    def update_rect(self, pos_x, pos_y):
        self.hitbox_rect = Rect(pos_x, pos_y, self.size_x, self.size_y)
        self.pos_x = pos_x
        self.pos_y = pos_y

    def check_collide(self, entity):
        if self.hitbox_rect.colliderect(entity.hitbox_rect) == True:
            return True
        else: 
            return False