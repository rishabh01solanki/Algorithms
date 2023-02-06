# this program determines if a number is even or odd
# it uses the concept of binary numbers and bitwise operators

def even(num):

    if num is float:
        raise ValueError("Number is a float, Enter an integer")
    else:
    # num & 1 will do the bitwise and operation on the 0th bits of the num and 1
    # which will return true only is the number is odd. use the not operator to 
    # get the result.
        if not num & 1:
            return ("{} is even".format(num))
        else:
            return ("{} is odd".format(num))

print(even(9))