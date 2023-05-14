# this program determines if a number is even or odd
# it uses the concept of binary numbers and bitwise operators
import time 

def even(num):

    
    # num & 1 will do the bitwise and operation on the 0th bits of the num and 1
    # which will return true only is the number is odd. use the not operator to 
    # get the result.
    return not num & 1

       

def better_even(num):
    return num % 2 == 0

start = time.time()

for i in range(100000):
    even(214317924802347017324303912784907)

print (time.time()-start)

start = time.time()

for i in range(100000):
    better_even(214317924802347017324303912784907)

print (time.time()-start)
