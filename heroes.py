from character import Character;


class Fighter(Character):
	def __init__(self):
		self.name = "Tough-guy"
		self.type = "Fighter";
		self.max_health = 1000;
		self.current_health = 1000;
		self.power = 90;
		self.bonus_damage = 1.2

class Wizard(Character):
	def __init__(self):
		self.name = "Merlin"
		self.type = "Wizard";
		self.max_health = 700;
		self.current_health = 700;
		self.power = 80;
		self.bonus_damage = 1.8
