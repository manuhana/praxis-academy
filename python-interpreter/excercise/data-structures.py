# list
day_name = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

# operating list
# count
day_name.count('sunday')
day_name.count('saturday')

# index
day_name.index('thursday')
day_name.index('sunday')

# reverse
day_name.reverse()
day_name

# append
day_name.append('holidays')
day_name

# sort
day_name.sort()
day_name

# pop
day_name.pop()
day_name

# lists as stack
stack_1 = [13, 18, 21]
stack_1.append(33)
stack_1.append(12)
stack_1
stack_1.pop()
stack_1

# lists as queues
from collections import deque
queue = deque(['monkey', 'snake', 'elephant', 'dragon'])
queue.append('fish')
queue.append('ant')
queue.popleft()
queue

# lists comprehension
power_three = []
for x in range(10):
    power_three.append(x**3)
power_three

# similar as
power_three = [x**3 for x in range(10)]
power_three

# tupples
tup_one = 'ceb', 'ana', 666
tup_two = tup_one, ('notail', 'jerax', 999)
tup_two

# sets
set_1 = set(wkwkwkwk)
set_2 = set(okokokok)
set_1
set_2
set_1 ^ set_2

# dictionaries
exp = {'ana': 12, 'ceb': 7, 'notail': -1, 'ban': 0}
exp['ana']
del exp['ban']
exp

# other ways
exp_2([('ban', 18), ('dea', 21), ('zack', 33)])
exp_2

# or
exp_3(miracle=9856, ana=9722, pevo=1282)
exp_3