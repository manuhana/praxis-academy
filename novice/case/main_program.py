# this is the main_program for importing sorts algorithm
# import all algorithm sort as module
import selection_sort
import merge_sort
import insertion_sort
import counting_sort
import bubble_sort

# how to use selection sort
# give nlist as an input list to sort
nlist = [9, 12, 98, 17, 22, 3]
selection_sort.selectionsort(nlist)
print(nlist)

# how to use merge sort
# give nlist as an input list to sort
nlist = [23, 88, 98, 99, 12, 18, 71, 4]
merge_sort.mergesort(nlist)
print(nlist)

# how to use insertion sort
# give 'data' as an input list to sort
data = [3, 8, 12, 98, 92, 64, 23, 10]
insertion_sort.insertion(data)
print(data)

# how to use counting sort
# give nlist as an input list to sort
# and an integer to set it as maximum value
nlist = [1, 4, 1, 2, 2, 5, 2]
max_value = 7
counting_sort.counting_sort(nlist, max_value)
print(nlist)

# how to use bubble sort
# give nlist as an input list to sort
# remember that this bubble sort is sorting value from the biggest one to the lowest
nlist = [71, 66, 28, 83, 90, 10]
bubble_sort.bubble_sort(nlist)
print(nlist)
