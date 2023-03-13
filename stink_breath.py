from random import randint
class Stink_Breath:
    """A basic attack."""

    def __init__(self):
        self.name ="STINK BREATH"
        self.start_PP = 4
        self.PP = self.start_PP

    def atk_damage(self):
        self.damage = randint(-10, -5)
        if self.PP >= 0:
            self.PP -= 1
            return self.damage
        else:
            print("No more PP left for this move!")
            return 0