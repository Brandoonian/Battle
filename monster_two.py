class Monster_TWO:
    """A class to manage monster2"""

    def __init__(self):
        """Initialize monster and it's attributes"""
        self.name = "UltraSteve"
        self.HP = 101
        self.attack_1()
        self.attack_2()
        self.attack_3()
        self.attack_4()

    def chosen_2(self):
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
        self.attack_1_name = "WEGDIE"
        self.damage = -10
        return self.damage

    def attack_2(self):
        """Characteristics of this attack."""
        self.attack_2_name = "BUTTFUCK"
        self.damage = -15
        return self.damage

    def attack_3(self):
        """Characteristics of this attack."""
        self.attack_3_name = "SCRATCH"
        self.damage = -15
        return self.damage

    def attack_4(self):
        """Characteristics of this attack."""
        self.attack_4_name = "SCREECH"
        self.damage = -15
        return self.damage