class BaseMonster:

	def check_hp(self):
		if self.HP <= 0.0:
			print(f"{self.name} has been defeated.")
			return False
		else:
		    return True

	def chosen(self):
		"""Tells user they have chosen this monster."""
		print(f"\nYou have chosen {self.name}!")

	def attack_1_effect(self):
		return None

	def attack_2_effect(self):
		return None



	def attack_4_effect(self):
		return None