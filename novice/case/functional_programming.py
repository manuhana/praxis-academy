def Greeting(one): # invoke the function
	print("Hello World")
	return one.upper()

Greeting("Oke") # call the function
# adding function attributes // this phase doesn't work
# Oke = Greeting(one) // this phase doesn't work
# print(Oke("English")) // this phase doesn't work

def square(x):
	return x * x
area = square(5)
print(area)

foo = square
foo(6)
print(foo(6))

# passing function as parameter
def formalGreeting():
	print("How are you?")

def casualGreeting():
	print("What's up?")

def greet(type, greetFormal, greetCasual):
	if type == "formal":
		greetFormal()
	elif type == "casual":
		greetCasual()

greet("casual", formalGreeting, casualGreeting)

# high order function
arr1 = [1, 2, 3]; arr2 = list(map(lambda x: x * 2, arr1))
print(arr2)
# without high order function
arr1 = [1, 2, 3]
arr2 = []
for x in arr1:
	ver = x * 2
	arr2.append(ver)
print(arr2)

# again, this is another example non-high order function
birthYear = [1975, 1997, 2002, 1995, 1985]
ages = []
for x in range(len(birthYear)):
	age = 2018 - birthYear[x]
	ages.append(age)
print(ages)
# with high order function
ages = list(map(lambda x: 2018 - x, birthYear)) # this birthYear is same as before
print(ages)

# again, without high order function
persons = {
	"Peter" : 16,
	"Mark" : 18,
	"John" : 27,
	"Jane" : 14,
	"Tony" : 24}
print(persons)
full_age = 0
for y in persons.values():
	if y >= 18:
		full_age += y
print(full_age)
# and now, using the high order function called "filter"
persons = {
	"Peter" : 16,
	"Mark" : 18,
	"John" : 27,
	"Jane" : 14,
	"Tony" : 24}
full_age = sum(filter(lambda x: x >= 18, persons.values()))
print(full_age)

# another example of non-high order function
arr = [5, 7, 1, 8, 4]
Sum = 0
for x in arr:
	Sum += x
print(Sum)
# now using high order function called "reduce"
from functools import reduce
Sum = reduce((lambda x, y: x + y), arr)
print(Sum)

# extra exercise!
strArray = ["JavaScript", "Python", "PHP", "Java", "C"]
def mapForEach(arrn):
	newArray = []
	for i in strArray:
		y = len(i)
		newArray.append(y)
	return newArray
lengthArray = mapForEach(strArray)
print(lengthArray)
# using high order function // this problem didn't solved yet
# strArray = ["JavaScript", "Python", "PHP", "Java", "C"]
# lenx = [len(x) for x in strArray]
# lengthArray = map((lambda x, y: y == len(x)), strArray, lenx)
# print(lengthArray)