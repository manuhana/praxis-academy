import math
li = [4, 9, 16, 25, 36]
x = list(map(math.sqrt, li))
print(x)

og = ['notail', 'jerax', 'ana', 'ceb', 'topson']
og.sort()
og
og.sort(key= lambda x: x.upper)
og