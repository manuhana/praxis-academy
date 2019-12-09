print('###################################')
print('Welcome to Manuhana ATM!')
print('###################################')

# let's get started with parent class
class atm:
	def __init__(self):
		self.name = input('Please insert your name: ')
		self.welcome = 'Welcome, ' + self.name.title() + ' !'
		print(self.welcome)
	
	def security(self):
		self.pin = input('Please input your pin here: ')
		self.pin_1 = '123456'
		while self.pin != self.pin_1:
			print('Your pin is wrong!')
			self.pin = input('Please type your pin: ')
		print('Access granted!')

manuhana = atm()
manuhana.security()
