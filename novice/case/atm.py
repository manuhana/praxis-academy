# classing machine opening
print('###################################')
print('Welcome to Manuhana ATM!')
print('###################################')

# let's get started with welcome menu
print('Do you have an account?')
print('[1] Yes')
print('[2] No, I want to sign up now')
decide = input()

# main menu for login or sign up
if decide == '1':
	# existing account
	x_username = input('Please input your username : ')
	x_pin = input('Please input your pin number : ')
	print('Welcome,', x_username.title() + '!')

else:
	# create new account
	username = input('Please input a username : ')
	print('Please create your 6 number of pin')
	pin = input()
	print('Welcome,', username.title() + '!')

# lets make a client database
client = {}