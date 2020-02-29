import random

class Player:

	def __init__(self, NoPoint): # Player constructor

		self.NoPoint = NoPoint  # Number of point of the player, this could be init based on our choice
		self.Alive = True      # Player start alive

	def getNoPoint(self):  
		return self.NoPoint  # Get function

	def setNoPoint(self, NoPoint): # Set Function 
		self.NoPoint = NoPoint
		if NoPoint > 0:
			self.Alive = True
		else:
			self.Alive = False

	def Attack(self, monster):   # Attack function based on the Dice Launch

		PlayerLaunch = self.PlayerLaunchDice()
		MonsterLaunch = monster.MonsterLaunchDice()

		if(PlayerLaunch >= MonsterLaunch):
			monster.getDamaged()

	def PlayerLaunchDice(self):  # Launch Dice for player
		return random.randint(1,6)


	def getDamaged(self, damage):  # Damaging the play after an attack 
		value = random.randint(1, 6)
		if value > 2:					# Game rules: Some defense for the player 
			self.NoPoint -= damage

		if self.NoPoint < 0:    # Player dies if NoPoint < 0 
			self.Alive = False

	



class EasyMonster:  # Eeasy Monster 

	def __init__(self):
		self.damage = 10  # Damage that could cause to a player 
		self.Alive = True  # Live status 

	def getAlive(self):  # Get Alive function 
		return self.Alive

	def setAlive(self, Alive): # Set Alive function 
		self.Alive = Alive

	def Attack(self, player):  # Eesy Monster attack based on the Dice Launch
		MonsterLaunch = self.MonsterLaunchDice()
		PlayerLaunch = player.PlayerLaunchDice()

		if (MonsterLaunch > PlayerLaunch):
			player.getDamaged(self.damage)

	def getDamaged(self):  # Damaging the monster 
		self.setAlive(False)

	def MonsterLaunchDice(self):  # Monster Launch Dice
		return random.randint(1, 6)


class DifficultMonster(EasyMonster) :  # Difficult Monster Inherit from Easy Monster 

	def __init__(self):            # Constructor 
		EasyMonster.__init__(self)  # Getting EasyMonster Attributes and methodes 
		self.damageSort = 5  # More damaging

	def AttackMonster(self, player):  # Difficult Monster Attack 

		self.Attack(player)

		value = self.MonsterLaunchDice()
		if value == 6: 						# Game rules 
			value = 0
		else: 
			value = self.damageSort*value

		player.getDamaged(value)  # damaging the player 
