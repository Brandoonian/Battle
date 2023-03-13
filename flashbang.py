from random import randint
class Flashbang:
    """A basic attack."""

    def __init__(self):
        self.name ="FLASHBANG"
        self.start_PP = 2
        self.PP = self.start_PP

    def atk_damage(self):
        self.damage = randint(-15, -10)
        if self.PP >= 0:
            self.PP -= 1
            return self.damage
        else:
            print("No more PP left for this move!")
            return 0