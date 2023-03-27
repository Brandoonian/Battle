from random import randint
class Flashbang:
    """A basic attack."""

    def __init__(self):
        self.name ="FLASHBANG"

        self.start_PP = 2
        self.PP = self.start_PP

        self.move_acc = 89.85

    def atk_damage(self):
        self.damage = randint(-15, -10)
        if self.PP >= 0:
            self.PP -= 1
            return self.damage
        else:
            print("No more PP left for this move!")
            self.PP -= 1
            return 0

    def atk_effect(self):
        self.dict = {
            "name": "blinded",
            "blinding": (90/100),
            "active": False}
        if self.PP >= -1:
            return self.dict
        else:
            return None