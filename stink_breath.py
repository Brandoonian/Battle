from random import randint
class Stink_Breath:
    """A basic attack."""

    def __init__(self):
        self.name ="STINK BREATH"

        self.start_PP = 4
        self.PP = self.start_PP

        self.move_acc = 89.85

    def atk_damage(self, damage):
        self.damage = randint(-10, -5)
        if self.PP >= 0:
            self.PP -= 1
            return self.damage
        else:
            print("No more PP left for this move!")
            return 0

    def atk_effect(self):
        self.dict = {
            "name": "poisoned",
            "duration_set": False,
            "duration": randint(3, 4),
            "odds": 20,
            "damage": randint(-4, -2),
            "active": False}
        if self.PP >= 0:
            return self.dict
        else:
            return None






