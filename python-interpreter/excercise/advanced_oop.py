class dog():
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def run(self):
		print(self.name.tittle() + ' is now running!')
		
	def sit(self):
		print(self.name.tittle() + ' is now sitting!')
