class Food:
	def __init__(self, x, y, habitat):
		self.x = x
		self.y = y
		self.habitat = habitat
		self.consumerList = []

	def __repr__(self):
		return f"position: {self.x, self.y}"

	def fightForMe(self, org1, org2):
		#here goes the logic of wisdom
		winner, loser = sorted([org1, org2], key=lambda x:x.size, reverse=True)
		self.consumerList.remove(loser)
		loser.health -= self.habitat.costOfFight


	def eaten(self):
		if len(self.consumerList)==1:
			self.consumerList[0].consume(self)
			self.habitat.food.remove(self)
		else:
			org1, org2 = self.consumerList[0], self.consumerList[1]
			self.fightForMe(org1, org2)