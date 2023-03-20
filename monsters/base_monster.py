class BaseMonster:
	def attack_2_effect(self):
		return None

	def check_hp(self):
		if self.HP <= 0.0:
			print(f"{self.name} has been defeated.")
			return False
		else:
		    return True