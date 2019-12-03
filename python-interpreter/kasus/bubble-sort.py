def bubble_sort(nlist):
    for a in range(len(nlist)-1,0,-1):
        for i in range(a):
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp