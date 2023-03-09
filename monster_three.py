class Monster_THREE:
    """A class to manage monster3"""

    def __init__(self):
        """Initialize monster and it's attributes"""
        self.name = "AlphaChet"
        self.HP = 102
        self.attack_1()
        self.attack_2()
        self.attack_3()
        self.attack_4()

    def chosen_3(self):
        """Tells user they have chosen this monster."""
        print(f"\nYou have chosen {self.name}!")

    def check_hp(self):
        if self.HP <= 0:
            print(f"{self.name} has been defeated.")
            return False
        else:
            return True

    def attack_1(self):
        """Characteristics of this attack."""
        self.attack_1_name = "BELLY SLAM"
        self.damage = -9
        return self.damage

    def attack_2(self):
        """Characteristics of this attack."""
        self.attack_2_name = "TIDDY TWISTER"
        self.damage = -14
        return self.damage

    def attack_3(self):
        """Characteristics of this attack."""
        self.attack_3_name = "RUSTY HOOK"
        self.damage = -15
        return self.damage

    def attack_4(self):
        """Characteristics of this attack."""
        self.attack_4_name = "SHIT BREATH"
        self.damage = -15
        return self.damage