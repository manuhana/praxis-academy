def look():
	a = []
	b = input('Please input your number : ')
	for t in range(int(b)):
		a.append(t*2)
		t += 1
		print(a)
x = look()

# without high order function
def substract(f,g):
	return f + g
f = 3
g = 9
print(substract(f,g))
# with simple high order function "lambda"
lambda f,g:f + g