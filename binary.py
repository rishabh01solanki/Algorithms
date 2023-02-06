# program that prints the binary value of a number in base 10 (normal) system

def binary(num):
    
    # base case, whenver we use recursion, we must move towards the base case
    if(num > 1):
        binary(num // 2)
    print(num % 2, end=' ')

print (binary(10))