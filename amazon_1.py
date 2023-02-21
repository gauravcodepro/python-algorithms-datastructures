#Determine if the sum of two integers is equal to the given value
#Given an array of integers and a value, determine if there are any two integers in the array whose 
#sum is equal to the given value. Return true if the sum exists and return false if it does not.
a=[5,7,1,2,8,4,3] 
b=10
# Return those values whose sum is not equal to the int present in the list
[sorted((b-n) for n in a if b-n not in a)]
#Return all possible combination of the int whose sum is equal to the defined int
[sorted((b-n) for n in a if b-n in a)]
[6,9]
[5, 3, 8, 2, 7]

# Merge two sorted linked lists.Given two sorted linked lists, merge them so that the resulting linked list is also sorted. 
# Consider two sorted linked lists and the merged list below them as an example
a = [4,8,15,19,'Null']
b = [7,9,10,16,'Null']
print(list(zip(a,b)))
[(4, 7), (8, 9), (15, 10), (19, 16), ('Null', 'Null')]

#Find the missing number in the array:You are given an array of positive numbers from 1 to n, such that all numbers 
# from 1 to n are present except one number x. You have to find x. The input array is not sorted
a=[3,7,1,2,8,4,5]
b=[]
sorted(a)
for i in range(len(a)):
    b.append(i+1)
for num in a:
    for j in b:
        if j not in a:
            print(j)
[6]

#Find all subsets of a given set of integers.We are given a set of integers and we have to find all the possible 
# subsets of this set of integers
a=[2,3,4]
from more_itertools import substrings
print(list(substrings(a)))
[(2,), (3,), (4,), (2, 3), (3, 4), (2, 3, 4)]

#Find Kth permutation.Given a set of ‘n’ elements, find their Kth permutation. Consider the following set of elements
a=[1,2,3]
from itertools import permutations
b=permutations(a)
print(list(b))
[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]