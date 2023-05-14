# Given a list containing numbers and a target number, 
# find all the combinations of two numbers from the list whose sum equals the target

# the time complexity for this approach is O(n)
def two_sum(a_list, target):
    
    a_dict = {}
    for index, num in enumerate(a_list):
        rem = target - num
        if rem in a_dict:
            return index, a_dict[rem]
        else:
            a_dict[num] = index

# here is a brute force method, time complexity is O(n^2)
def sum_two(a_list, target):

    for i in range(len(a_list)):
        for j in range(i, len(a_list)):
            if a_list[i] + a_list[j] == target:
                return a_list[i],a_list[j]
             


a_list = [num for num in range(1,10)]


a,b = two_sum( a_list, 10)
print(a_list[a],a_list[b])


a,b = sum_two(a_list, 10)
print(a,b)



