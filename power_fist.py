from random import randint
class Power_Fist:
    """A basic attack."""

    def __init__(self):
        self.name ="POWER FIST"
        self.start_PP = 3
        self.PP = self.start_PP

    def atk_damage(self):
        self.damage = randint(-12, -8)
        if self.PP >= 0:
            self.PP -= 1
            return self.damage
        else:
            print("No more PP left for this move!")
            return 0


