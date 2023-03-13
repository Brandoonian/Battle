from random import randint
class Screech:
    """A basic attack."""

    def __init__(self):
        self.name ="SCREECH"
        self.start_PP = 3
        self.PP = self.start_PP

    def atk_damage(self):
        self.damage = randint(-8, -5)
        if self.PP >= 0:
            self.PP -= 1
            return self.damage
        else:
            print("No more PP left for this move!")
            return 0