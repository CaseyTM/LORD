# class Dragon(object):
# 	def __init__(self):
# 		self.name = "Green Dragon";
# 		self.max_health = 600;
# 		self.current_health = 600;
# 		self.power = 50;
# 		self.bonus_damage = 1.5;
# 	def image(self):
# 		print "                                                  .~))>>"
# 		print "                                                 .~)>>"
# 		print "                                             .~))>>"             
# 		print "                                           .~))>>)))>>      .-~))>>  "
# 		print "                                         .~)))))>>       .-~))>>)>"
# 		print "                                       .~)))>>))))>>  .-~)>>)>"
# 		print "                   )                 .~))>>))))>>  .-~)))))>>)>"
# 		print "                ( )@@*)             //)>))))))  .-~))))>>)>"
# 		print "              ).@(@@               //))>>))) .-~))>>)))))>>)>"
# 		print "          ))  )@@*.@@ )          //)>))) //))))))>>))))>>)>"
# 		print "       ((  ((@@@.@@             |/))))) //)))))>>)))>>)>"
# 		print "      )) @@*. )@@ )   (\_(\-\b  |))>)) //)))>>)))))))>>)>"
# 		print "    (( @@@(.@(@ .    _/`-`  ~|b |>))) //)>>)))))))>>)>"
# 		print "     )* @@@ )@*     (@) (@)  /\b|))) //))))))>>))))>>"
# 		print "   (( @. )@( @ .   _/       /  \b)) //))>>)))))>>>_._"
# 		print "    )@@ (@@*)@@.  (6,   6) / ^  \b)//))))))>>)))>>   ~~-."
# 		print " ( @jgs@@. @@@.*@_ ~^~^~, /\  ^  \b/)>>))))>>      _.     `,"
# 		print "  ((@@ @@@*.(@@ .   \^^^/' (  ^   \b)))>>        .'         `,"
# 		print "   ((@@).*@@ )@ )    `-'   ((   ^  ~)_          /             `,"
# 		print "     (@@. (@@ ).           (((   ^    `\        |               `."
# 		print "       (*.@*              / ((((        \        \      .         `."
# 		print "                         /   (((((  \    \    _.-~\     Y,         ;"
# 		print '                        /   / (((((( \    \.-~   _.`" _.-~`,       ;'
# 		print "                       /   /   `(((((()    )    (((((~      `,     ;"
# 		print '                     _/  _/      `"""/   /"                  ;     ;'
# 		print "                 _.-~_.-~           /  /'                _.-~   _.'"
# 		print "               ((((~~              / /'              _.-~ __.--~"
# 		print "                                  ((((          __.-~ _.-~"
# 		print "                                              .'   .~~"
# 		print "                                              :    ,'"
# 		print "                                              ~~~~~"
		
# 	def alive(self):
# 		return self.current_health > 0;
# 	def take_damage(self, base_dmg_from_hero, bonus_from_hero):
# 		self.current_health -= (base_dmg_from_hero);
# 	def attack(self, hero):
# 		print "%s attacks %s for %d points of damage" % (self.name, hero.name, (self.power * self.bonus_damage))
# 		hero.take_damage(self.power, self.bonus_damage)



from character import Character;
class Dragon(Character):
	def __init__(self):
		self.name = "Green Dragon";
		self.max_health = 6000;
		self.current_health = 6000;
		self.power = 500;
		self.bonus_damage = 1.5;

	def image(self):
		print "                                                  .~))>>"
		print "                                                 .~)>>"
		print "                                             .~))>>"             
		print "                                           .~))>>)))>>      .-~))>>  "
		print "                                         .~)))))>>       .-~))>>)>"
		print "                                       .~)))>>))))>>  .-~)>>)>"
		print "                   )                 .~))>>))))>>  .-~)))))>>)>"
		print "                ( )@@*)             //)>))))))  .-~))))>>)>"
		print "              ).@(@@               //))>>))) .-~))>>)))))>>)>"
		print "          ))  )@@*.@@ )          //)>))) //))))))>>))))>>)>"
		print "       ((  ((@@@.@@             |/))))) //)))))>>)))>>)>"
		print "      )) @@*. )@@ )   (\_(\-\b  |))>)) //)))>>)))))))>>)>"
		print "    (( @@@(.@(@ .    _/`-`  ~|b |>))) //)>>)))))))>>)>"
		print "     )* @@@ )@*     (@) (@)  /\b|))) //))))))>>))))>>"
		print "   (( @. )@( @ .   _/       /  \b)) //))>>)))))>>>_._"
		print "    )@@ (@@*)@@.  (6,   6) / ^  \b)//))))))>>)))>>   ~~-."
		print " ( @jgs@@. @@@.*@_ ~^~^~, /\  ^  \b/)>>))))>>      _.     `,"
		print "  ((@@ @@@*.(@@ .   \^^^/' (  ^   \b)))>>        .'         `,"
		print "   ((@@).*@@ )@ )    `-'   ((   ^  ~)_          /             `,"
		print "     (@@. (@@ ).           (((   ^    `\        |               `."
		print "       (*.@*              / ((((        \        \      .         `."
		print "                         /   (((((  \    \    _.-~\     Y,         ;"
		print '                        /   / (((((( \    \.-~   _.`" _.-~`,       ;'
		print "                       /   /   `(((((()    )    (((((~      `,     ;"
		print '                     _/  _/      `"""/   /"                  ;     ;'
		print "                 _.-~_.-~           /  /'                _.-~   _.'"
		print "               ((((~~              / /'              _.-~ __.--~"
		print "                                  ((((          __.-~ _.-~"
		print "                                              .'   .~~"
		print "                                              :    ,'"
		print "                                              ~~~~~"
		