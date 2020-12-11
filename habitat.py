import os
from utilities import getFixedInput
import random
from food import Food
from organism import Organism

class Habitat:
	def __init__(self, length=100, initialFoodCount=200):
		self.length = length
		self.originalOrganisms = []
		self.organisms = []
		self.food = []
		self.costOfMoving = 11.5
		self.costOfFight = 3*self.costOfMoving
		self.speed_a = 10   # all these values will be chnaged later.
		self.sense_a = 10  # all these values will be chnaged later.
		self.wisdom_a = 10  # all these values will be chnaged later.
		self.size_a = 10    # all these values will be chnaged later.



	def createPlayer(self):
		money = 40
		print('You have 40 to spend on the four traits: speed, sense, wisdom, size.\nIf you dont follow the limit for traits the program might crash and you might lose the data \n')
		input('press any key to continue')
		os.system('clear')
		speedp, sensep, wisdomp, sizep = getFixedInput(5, 15, 40)
		player = Organism(speed, sensep, wisdomp, sizep, 0, 34, 'player')
		self.originalOrganisms.append(player)
		self.organisms.append(player)
		




	def placeOrganisms(self):
		for i in range(20):
			a = random.randrange(0, 100)
			o1 = Organism(self.speed_a, self.sense_a, self.wisdom_a, self.size_a, 0, a)
			o2 = Organism(self.speed_a, self.sense_a, self.wisdom_a, self.size_a, a, 0)
			o3 = Organism(self.speed_a, self.sense_a, self.wisdom_a, self.size_a, 100, a)
			o4 = Organism(self.speed_a, self.sense_a, self.wisdom_a, self.size_a, a, 100)
			self.originalOrganisms.append(o1)
			self.originalOrganisms.append(o2)
			self.originalOrganisms.append(o3)
			self.originalOrganisms.append(o4)
			self.originalOrganisms.append(o1)
			self.originalOrganisms.append(o2)
			self.originalOrganisms.append(o3)
			self.originalOrganisms.append(o4)





	def simulateDay(self):
		for i in range(self.foodCount):
			x = random.randint(0, self.length)
			y = random.randint(0, self.length)
			a = Food(x, y)
			self.food.append(a)


	def startSimulation(self):
		placeOrganisms()
		createPlayer()


		while self.organisms:
			while self.food:
				# here goes the daily(in game) logic
				pass