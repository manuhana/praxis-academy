def selectionsort(nlist):
  for i in range(len(nlist)):
    minimum = i
    for k in range(i + 1 , len(nlist)):
      if nlist[k] < nlist[minimum]:
        minimum = k
 
    swap(nlist, minimum, i)
  
def swap(A, x, y):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp
