from random import randint
class Cold_Cut:
    """A basic attack."""

    def __init__(self):
        self.name ="COLD CUT"

        self.start_PP = 3
        self.PP = self.start_PP

        self.move_acc = 78.13

    def atk_damage(self):
        self.damage = randint(-20, -15)
        if self.PP >= 0:
            self.PP -= 1
            return self.damage
        else:
            print("No more PP left for this move!")
            return 0

    def atk_effect(self):
        self.dict = {
            "name": "frozen",
            "duration_set": False,
            "duration": randint(2, 4),
            "odds": 20,
            "damage": randint(-5, -3),
            "active": False}
        if self.PP >= 0:
            return self.dict
        else:
            return None