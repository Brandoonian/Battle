from scratch import Scratch
from screech import Screech
from cold_cut import Cold_Cut
from flashbang import Flashbang
from random import randint
from monsters.base_monster import BaseMonster

screech = Screech()
scratch = Scratch()
cold_cut = Cold_Cut()
flashbang = Flashbang()

class Monster_TWO(BaseMonster):
    """A class to manage monster3"""

    def __init__(self):
        """Initialize monster and it's attributes"""
        self.name = "UltraSteve"
        self.HP = 99.0
        self.accuracy = 97.0
        self.attack_1()
        self.attack_2()
        self.attack_3()
        self.attack_4()

    def attack_1(self):
        """Characteristics of this attack."""
        self.attack_1_name = scratch.name
        damage = scratch.atk_damage()
        return damage

    def display_PP_1(self):
        """Display PP for the move in attack_1 slot."""
        return f"({scratch.PP + 1}/{scratch.start_PP})"

    def attack_2(self):
        """Characteristics of this attack."""
        self.attack_2_name = screech.name
        damage = screech.atk_damage()
        return damage
    def attack_2_effect(self):
        forward = {
            "name": "confused",
            "duration_set": False,
            "duration": randint(2, 4),
            "odds": 20,
            "damage": randint(-5, -3),
            "active": False}
        return forward

    def display_PP_2(self):
        """Display PP for the move in attack_1 slot."""
        return f"({screech.PP + 1}/{screech.start_PP})"

    def attack_3(self):
        """Characteristics of this attack."""
        self.attack_3_name = cold_cut.name
        damage = cold_cut.atk_damage()
        return damage

    def attack_3_effect(self):
        forward = {
            "name": "frozen",
            "duration_set": False,
            "duration": randint(2, 4),
            "odds": 20,
            "damage": randint(-5, -3),
            "active": False}
        return forward

    def display_PP_3(self):
        """Display PP for the move in attack_1 slot."""
        return f"({cold_cut.PP + 1}/{cold_cut.start_PP})"

    def attack_4(self):
        """Characteristics of this attack."""
        self.attack_4_name = flashbang.name
        damage = flashbang.atk_damage()
        return damage

    def attack_4_effect(self):
        forward = {
            "name": "blinded",
            "blinding": (90/100),
            "active": False}
        return forward

    def display_PP_4(self):
        """Display PP for the move in attack_1 slot."""
        return f"({flashbang.PP + 1}/{flashbang.start_PP})"