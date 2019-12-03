# defining list
xlist = [2,7,9,13,8,21]

# insertionlist function
def insertionlist (xlist):
    for x in range (1,len(xlist)):
        tmp = xlist[x]
        k = x
        while k > 0 and tmp < xlist[k-1]:
            xlist[k] = xlist[k-1]
            k -= 1
        xlist[k] = tmp

# run insertionlist function
insertionlist(xlist)

# print out the result
print(xlist)
