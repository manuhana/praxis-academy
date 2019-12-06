class player():
	def __init__(self, name):
		self.name = name
		print('The player name is ' + self.name.title())
		
	def role(self):
		raise

class og(player):
	def role(self):
		return self.name.title() + ' role is carry!'

class liquid(player):
	def role(self):
		return self.name.title() + ' role is support!'

ana = og('ana')
kuroky = liquid('kuroky')
print(ana.role())
print(kuroky.role())
