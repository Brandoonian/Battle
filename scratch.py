from random import randint
class Scratch:
    """A basic attack."""

    def __init__(self):
        self.name ="SCRATCH"

        self.start_PP = 3
        self.PP = self.start_PP

        self.move_acc = 89.85

    def atk_damage(self):
        self.damage = randint(-15, -10)
        if self.PP >= 0:
            self.PP -= 1
            return self.damage
        else:
            print("No more PP left for this move!")
            return 0