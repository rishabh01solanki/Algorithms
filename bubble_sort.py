def bubble_sort(li):
    
    # assigning the length of the list
    length = len(list)-1
    
    # main outer loop starts
    for i in range(length):
        #inner loop starts
        no_swap = True
        for j in range(length-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1] = li[j+1],li[j]  #swap
                no_swap = False
        if no_swap:
            return li
    return li