class Player:


	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.speed = 1
		self.total = 0
		self.tail = []


	def update(self, speed, dirs, space):
		# 1 : up
		# 2 : right
		# 3 : down
		# 4 : left		
		if dirs == 1:
			self.y -= speed*space
		elif dirs == 2:
			self.x += speed*space
		elif dirs == 3:
			self.y += speed*space
		elif dirs == 4:
			self.x -= speed*space


	def eat(self, rect1, rect2):
		if rect1.colliderect(rect2):


			return True
		else:
			return False


	def tail_collide(self):
		# NOT WORKING
		for pos in self.tail:
			if self.x == pos[0] and self.y == pos[1]:
				return True
			else:
				return False


