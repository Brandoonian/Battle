from random import randint
class Cold_Cut:
    """A basic attack."""

    def __init__(self):
        self.name ="COLD CUT"
        self.start_PP = 1
        self.PP = self.start_PP

    def atk_damage(self):
        self.damage = randint(-20, -15)
        if self.PP >= 0:
            self.PP -= 1
            return self.damage
        else:
            print("No more PP left for this move!")
            return 0