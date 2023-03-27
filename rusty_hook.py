from random import randint
class Rusty_Hook:
    """A basic attack."""

    def __init__(self):
        self.name ="RUSTY HOOK"

        self.start_PP = 3
        self.PP = self.start_PP

        self.move_acc = 80.47

    def atk_damage(self):
        self.damage = randint(-20, -15)
        if self.PP >= 0:
            self.PP -= 1
            return self.damage
        else:
            print("No more PP left for this move!")
            return 0