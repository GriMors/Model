from demon import Demon
from cult import Cult
from berserk import Berserk
from world import World

class Model:

    def __init__(self):
        self.world = World(self)

    def collision(self, object1, object2):
        if type(object1) == Cult:
            if type(object2) == Demon:
                if object1.population():
                    object1.settlers += 1
                    object2.body.deleted = True
                    object2.circle.kill()
            elif type(object2) == Berserk:
                self.fight(object1, object2)

    def fight(self, object1, object2):
        if object1.settlers > object2.power:
            object2.body.deleted = True
            object2.circle.kill()
            object1.settlers -= 3
        else:
            object1.settlers -= 6
            object1.child = 0
            object1.body.deleted = True
            object1.circle.kill()