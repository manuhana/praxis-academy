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