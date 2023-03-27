from random import randint
class Nut_Punch:
    """A basic attack."""

    def __init__(self):
        self.name ="NUT PUNCH"

        self.start_PP = 4
        self.PP = self.start_PP

        self.move_acc = 78.13

    def atk_damage(self):
        self.damage = randint(-25, -17)
        if self.PP >= 0:
            self.PP -= 1
            return self.damage
        else:
            print("No more PP left for this move!")
            return 0

    def atk_effect(self):
        self.dict = {
            "name": "paralyzed",
            "duration_set": False,
            "duration": randint(1, 2),
            "odds": 20,
            "damage": 0,
            "active": False}
        if self.PP >= 0:
            return self.dict
        else:
            return None