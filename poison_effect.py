
from random import randint
import battle_main
class Poison_Effect:
    """A class to manage effects in the main loop."""

    def __init__(self):
        self.name = "poisoned"
        self.odds = randint(0, 4)
        self.duration = randint(2, 4)
        self.damage = randint(-4, -1)
        self.disable = False





