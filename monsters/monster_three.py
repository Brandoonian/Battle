from belly_slam import Belly_Slam
from rusty_hook import Rusty_Hook
from stink_breath import Stink_Breath
from brace import Brace
from monsters.base_monster import BaseMonster

belly_slam = Belly_Slam()
rusty_hook = Rusty_Hook()
stink_breath = Stink_Breath()
brace = Brace()

class Monster_THREE(BaseMonster):
    """A class to manage monster3"""

    def __init__(self):
        """Initialize monster and it's attributes"""
        self.name = "AlphaChet"
        self.HP = 102.0
        self.accuracy = 95.0
        self.evasion = 0.95
        self.attack_1()
        self.attack_2()
        self.attack_3()
        self.attack_4()

    def attack_1(self):
        """Characteristics of this attack."""
        self.attack_1_name = belly_slam.name
        damage = belly_slam.atk_damage()
        return damage

    def attack_1_acc(self):
        forward = belly_slam.move_acc
        return forward

    def display_PP_1(self):
        """Display PP for the move in attack_1 slot."""
        return f"({belly_slam.PP + 1}/{belly_slam.start_PP})"

    def attack_2(self):
        """Characteristics of this attack."""
        self.attack_2_name = rusty_hook.name
        damage = rusty_hook.atk_damage()
        return damage

    def attack_2_acc(self):
        forward = rusty_hook.move_acc
        return forward

    def display_PP_2(self):
        """Display PP for the move in attack_1 slot."""
        return f"({rusty_hook.PP + 1}/{rusty_hook.start_PP})"

    def attack_3(self):
        """Characteristics of this attack."""
        self.attack_3_name = stink_breath.name
        damage = stink_breath.atk_damage(damage=None)
        return damage

    def attack_3_effect(self):
        forward = stink_breath.atk_effect()
        return forward

    def attack_3_acc(self):
        forward = stink_breath.move_acc
        return forward

    def display_PP_3(self):
        """Display PP for the move in attack_1 slot."""
        return f"({stink_breath.PP + 1}/{stink_breath.start_PP})"

    def attack_4(self):
        """Characteristics of this attack."""
        self.attack_4_name = brace.name
        damage = brace.atk_damage()
        return damage

    def attack_4_effect(self):
        forward = brace.atk_effect()
        return forward

    def attack_4_acc(self):
        forward = brace.move_acc
        return forward

    def display_PP_4(self):
        """Display PP for the move in attack_1 slot."""
        return f"({brace.PP + 1}/{brace.start_PP})"