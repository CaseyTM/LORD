from character import Character;
from bosses import *;
from heroes import *;



level = "Start";

dragon = Dragon();
# dragon.test();

while 1:
	while (level == "Start"):
		print "Welcome to Casey's game"
		print "Please choose your class"
		print "1. I would like to be a FIGHTER, tough as nails!"
		print "2. I would like to be a WIZARD, glass cannon!"
		input = int(raw_input());
		if input == 1:
			player = Fighter();
			print "Congratulations, you have selected %s as your class, are you ready to proceed?" % player.type
			print "Press (1)to continue"
			input = int(raw_input());
			if input == 1:
				level = "Home";
			
		elif input == 2:
			player = Wizard();
			print "Congratulations, you have selected %s as your class, are you ready to proceed?" % player.type
			print "Press (1)to continue"
			input = int(raw_input());
			if input == 1:
				level = "Home";
		elif input == 10:
			print "you like Easter do you?"
		elif input != 1 or 2:
			print "You must make a valid selection"
		else:
			print "You must make a valid selection"




	while (level == "Home"):
		print "You wake up naked, alone and confused in the midst of the Forest"
		print "What's your next move?"
		print "Try to find my way to the (C)ity"
		print "Search the (F)orest for something to Kill"
		print "See if the (H)ealer is available"
		print "View your (S)tats"
		print "See your (I)nventory"
		input = raw_input();
		if input == "C":
			level = "City"
		elif input == "F":
			level = "Forest"
		elif input == "H":
			level = "Healer"
		elif input == "S":
			level = "Stats"
		elif input == "I":
			level == "Inventory"
		else:
			print "You must make a valid selection"



	while (level == "Forest"):
		print "You have entered the Forest, absolute silence greets you coldly"
		print "What actions would you like to take?"
		print "find monsters to (K)ill"
		print "(L)eave the forest and return from whence you came"
		print "(F)ollow the Giant footprints in the mud"
		input = raw_input();
		if input == "K":
			level = "Battlegrounds"
		elif input == "L":
			level = "Home"	
		elif input == "F":
			level = "Dragon"
		else:
			print "You must make a valid selection"


	while (level == "Dragon"):
		print "inside dragon loop";
		while player.alive() and dragon.alive():
			dragon.image()
			print "fighting dragon"
			print "You approach a large clearing in the forest, the trees are flattened and burned amidst a chaos of charred bodies. A massive cave entrance lies ahead, do you wish to proceed?"
			print "1. Take your chances"
			print "2. Run before the Dragon notices you"
			print dragon.name
			input = int(raw_input());
			print input
			if input == 1:
				player.attack(dragon);
				dragon.attack(player);
				print "Your HEALTH is currently %d of %d, the Dragon is at %d of %d" % (player.current_health, player.max_health, dragon.current_health, dragon.max_health);
				if player.alive():
					print "Victory"
					level = "Forest"
				else:
					print "You were slain by the %s" % dragon.name
					# print dragon.alive();
					level = "Home"
			elif input == 2:
				print "The %s chases you down but you barely escape!" % dragon.name
				level = "Forest"
				# break;
			else:
				print "You must enter a valid selection"
				break;
				


	while level == "Healer":
		print "you are at the Healer"
		

	while level == "City":
		print "you are at the City"
		break;













