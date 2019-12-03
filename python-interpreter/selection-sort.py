# defining list
xlist = [2,7,9,13,8,21,5]

# defining selection-sort function
def selectionsort( xlist ):
  for i in range( len( xlist ) ):
    minimum = i
    for k in range( i + 1 , len( xlist ) ):
      if xlist[k] < xlist[minimum]:
        minimum = k
 
    swap( xlist, minimum, i )
 
# making swap function 
def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp

# run selection-sort function
selectionsort(xlist)

# print out the result
print(xlist)