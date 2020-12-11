import random

class Organism:
	def __init__(self, speed, sense, wisdom, size, x, y, habitat, name=None):
		self.speed = speed
		self.sense = sense
		self.wisdom = wisdom
		self.size = size
		self.isDead = False
		self.parent = None
		self.childen = []
		self.food = 0
		self.health = 100
		self.x = x
		self.y = y
		self.habitat = habitat
		self.name = name

	def __repr__(self):
		return f"speed: {self.speed}\nsize: {self.size}\nsense: {self.sense}\nwisdom: {self.wisdom}\n"

	def die(self):
		self.isDead = True

	def move(self):
		self.health -= self.habitat.costOfMoving
		# moving in random dir logic goes here
		if True: #Condition for finding a food nearby if many chosing a random
			self.moveTowardsFood(food)

	def moveTowardsFood(self, food):
		self.health -= self.habitat.costOfMoving
		if True: # contition to check if the food is not in eating radius goes here
			self.moveTowardsFood(self)
		else:
			self.eat(food)

	def eat(self, food):
		# here goes the logic of wisdom
		food.consumerList.append(self)

	def consume(self, food):
		self.food += 1

	def reproduce(self):
		mutationFactor = 0.5
		speed = self.speed + ((random.random()-0.5)*self.speed/10)
		sense = self.sense + ((random.random()-0.5)*self.sense/10)
		wisdom = self.wisdom + ((random.random()-0.5)*self.wisdom/10)
		size = self.size + ((random.random()-0.5)*self.size/10)
		position_offset = (random.random()-0.5)*5 
		a = Organism(speed, sense, wisdom, size, self.x+position_offset, self.y+position_offset, self.habitat)
		a.parent = self
		self.child.append(a)
		self.habitat.organisms.append(a)
