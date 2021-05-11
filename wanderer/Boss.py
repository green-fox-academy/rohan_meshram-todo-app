from wanderer.Game_charcter import Game_charcter
from wanderer.wanderer import d6

class Boss(Game_charcter):

    def __init__(self, x: int, y: int,level):

        self.img = "boss"
        super().__init__(x,y,(2 * level * d6) + d6, (level / 2) * d6,(level * d6) + d6 )
