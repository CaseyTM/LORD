class Character(object):
	def take_damage(self, dmg_from_enemy):
		self.current_health -= (dmg_from_enemy);
	def attack(self, enemy):
		print "%s attacks %s for %d points of damage" % (self.name, enemy.name, (self.power * self.bonus_damage))
		enemy.take_damage(self.power * self.bonus_damage)
	def alive(self):
		return self.current_health > 0;

