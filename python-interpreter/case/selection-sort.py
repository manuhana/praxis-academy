def selectionsort( xlist ):
  for i in range( len( xlist ) ):
    minimum = i
    for k in range( i + 1 , len( xlist ) ):
      if xlist[k] < xlist[minimum]:
        minimum = k
 
    swap( xlist, minimum, i )
  
def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp
