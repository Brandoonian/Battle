from random import randint
class Super_Kick:
    """A basic attack."""

    def __init__(self):
        self.name = "SUPER KICK"

        self.start_PP = 2
        self.PP = self.start_PP

        self.move_acc = 89.85

    def atk_damage(self):
        self.damage = randint(-20, -15)
        if self.PP >= 0:
            self.PP -= 1
            return self.damage
        else:
            print("No more PP left for this move!")
            return 0