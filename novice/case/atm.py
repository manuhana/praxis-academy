# classing machine opening
print('######################################')
print('\tWelcome to Manuhana ATM!')
print('######################################')

# let's get started with welcome menu
print('Do you have an account?')
print('[1] Yes')
print('[2] No, I want to sign up now')
decide = input()

#  this will is the client username and pin database
client = {}

# create a new account
def sign_up():
	username = input('Please input a username : ')
	print('Please create your 6 number of pin')
	pin = input()
	# checking pin length
	while len(pin) != 6:
		print('Your pin number must be 6 number!')
		print('Please create your 6 number of pin')
		pin = input()
	print('Account created!')
	print('Welcome,', username.title() + '!')
	client[username] = pin
	return client

# login system
def login():
	username = input('Please input your username: ')
	print('Please input your pin number')
	pin = input()
	# lets check wether the username and pin are already registered

# lets back to decide action
if decide == '1':
	login()
else:
	sign_up()

# as far
