def counting_sort(nlist, max_value):
    m = max_value + 1
    count = [0] * m                
    
    for x in nlist:
        count[x] += 1             
    i = 0
    for x in range(m):            
        for c in range(count[x]):  
            nlist[i] = x
            i += 1
    return nlist