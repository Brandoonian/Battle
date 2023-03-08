class Monster_ONE:
    """A class to manage monter1"""

    def __init__(self):
        """Initialize monster and it's attributes"""
        self.HP = 100

    def attack_1(self):
        """Sets stats of first attck."""
        self.damage = 15
        return self.damage

    def lose_HP(self):
        """Allows for the loss of hit points."""
        #self.HP - opp_attack = new_HP


