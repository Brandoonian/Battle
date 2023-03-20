from power_fist import Power_Fist
from super_kick import Super_Kick
from nut_punch import Nut_Punch
from steel_toe import Steel_Toe
from random import randint


power_fist = Power_Fist()
super_kick = Super_Kick()
nut_punch = Nut_Punch()
steel_toe = Steel_Toe()

class Monster_ONE:
    """A class to manage monter1"""

    def __init__(self):
        """Initialize monster and it's attributes"""
        self.name = "GigaBob"
        self.HP = 99.0
        self.attack_1()
        self.attack_2()
        self.attack_3()
        self.attack_4()

    def chosen_1(self):
        """Tells user they have chosen this monster."""
        print(f"\nYou have chosen {self.name}!")

    def check_hp(self):
        if self.HP <= 0.0:
            print(f"{self.name} has been defeated.")
            return False
        else:
            return True

    def attack_1(self):
        """Characteristics of this attack."""
        self.attack_1_name = power_fist.name
        damage = power_fist.atk_damage()
        return damage

    def attack_1_effect(self):
        return None

    def display_PP_1(self):
        """Display PP for the move in attack_1 slot."""
        return f"({power_fist.PP + 1}/{power_fist.start_PP})"

    def attack_2(self):
        """Characteristics of this attack."""
        self.attack_2_name = super_kick.name
        damage = super_kick.atk_damage()
        return damage

    def attack_2_effect(self):
        return None

    def display_PP_2(self):
        """Display PP for the move in attack_1 slot."""
        return f"({super_kick.PP + 1}/{super_kick.start_PP})"

    def attack_3(self):
        """Characteristics of this attack."""
        self.attack_3_name = nut_punch.name
        damage = nut_punch.atk_damage()
        return damage

    def attack_3_effect(self):
        forward = {
            "name": "paralyzed",
            "duration_set": False,
            "duration": randint(1, 2),
            "odds": 20,
            "damage": 0,
            "active": False}
        return forward

    def display_PP_3(self):
        """Display PP for the move in attack_1 slot."""
        return f"({nut_punch.PP + 1}/{nut_punch.start_PP})"

    def attack_4(self):
        """Characteristics of this attack."""
        self.attack_4_name = steel_toe.name
        damage = steel_toe.atk_damage()
        return damage

    def attack_4_effect(self):
        return None

    def display_PP_4(self):
        """Display PP for the move in attack_1 slot."""
        return f"({steel_toe.PP + 1}/{steel_toe.start_PP})"