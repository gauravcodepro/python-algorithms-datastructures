#Permutations(Medium)
#The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
#By listing and labeling all of the permutations in order, 
# we get the following sequence for n = 3:
#"123"
#"132"
#"213"
#"231"
#"312"
#"321"
#Given n and k, return the kth permutation sequence.
#Example 1:
#Input: n = 3, k = 3
#Output: "213"
#Example 2:
#Input: n = 4, k = 9
#Output: "2314"
#Example 3:
#Input: n = 3, k = 1
#Output: "123"
#################################################
from itertools import permutations
a=[1,2,3]
k=k-1
[i[k] for i in [(list(permutations(a)))]]
################################
from itertools import permutations
a=[1,2,3,4]
k=k-1
[i[k] for i in [(list(permutations(a)))]]