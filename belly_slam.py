from random import randint
class Belly_Slam:
    """A basic attack."""

    def __init__(self):
        self.name ="BELLY SLAM"
        self.start_PP = 1
        self.PP = self.start_PP

    def atk_damage(self):
        self.damage = randint(-25, -20)
        if self.PP >= 0:
            self.PP -= 1
            return self.damage
        else:
            print("No more PP left for this move!")
            return 0

    def effect(self):
        None