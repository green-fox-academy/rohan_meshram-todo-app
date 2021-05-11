from wanderer.Game_charcter import Game_charcter
#from wanderer.wanderer import d6

from random import randint
class Hero(Game_charcter):

    def d6(self):
        d6 = randint(1, 6)
        return d6
    def __init__(self,level):

        self.img = "hero_down"
        super().__init__(0,0,20 + (3 * self.d6()),2 *self.d6() ,5 + self.d6() ,self.d6(),level)






    def move(self, x = 0, y = 0):
        self.x += x
        self.y += y
        if x == -1:
            self.img = "hero_left"
        elif x == 1:
            self.img = "hero_right"
        elif y == -1:
            self.img = "hero_up"
        elif y == 1:
            self.img = "hero_down"