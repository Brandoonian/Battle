from random import randint
class Effect:

    def __init__(self):
        self.name = "poison"
        self.odds = (0, 4)
        self.duration = randint(2, 4)
        self.damage = (-4,-2)
        self.disable False

    def check_effect():
        self.effect = user_monster.attack_3_effect()
        if effect == "poison":
            odds = randint(0, 4)
            if odds == 1 or 2 or 3 or 4:
                print(f"{cpu_monster.name} has been poisoned!")
                duration = randint(2, 4)