from character import Character;


class Monster(Character):
	def __init__(self):
		self.name = "Goblin"
		self.max_health = 500;
		self.current_health = 500;
		self.power = 50;
		self.bonus_damage = 1.3;