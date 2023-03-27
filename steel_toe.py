from random import randint
class Steel_Toe:
    """A basic attack."""

    def __init__(self):
        self.name ="STEEL TOE"

        self.start_PP = 2
        self.PP = self.start_PP

        self.move_acc = 85.94

    def atk_damage(self):
        self.damage = randint(-15, -10)
        if self.PP >= 0:
            self.PP -= 1
            return self.damage
        else:
            print("No more PP left for this move!")
            return 0