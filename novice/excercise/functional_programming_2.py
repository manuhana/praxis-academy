def look():
	a = []
	b = input('Please input your number : ')
	for t in range(int(b)):
		a.append(t*2)
		t += 1
		print(a)
x = look()