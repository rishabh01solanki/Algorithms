def insertion_sort(li):

    # main loop starts here
    for i in range(1,len(li)): 
        
        # stores the value
        value = li[i]

        while i>0 and value<li[i-1]:
            li[i] = li[i-1]   # swaps if left is smaller than the right 
            i -= 1
        li[i] = value
    
    return li