#Subsets II (Medium)
#Given an integer array nums that may contain duplicates, return all possible subsets(the power set).
#The solution set must not contain duplicate subsets. Return the solution in any order.
#Example 1:
#Input: nums = [1,2,2]
#Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
#Example 2:
#Input: nums = [0]
#Output: [[],[0]]
##### listing all the substrings ####
from more_itertools import substrings
nums = [1,2,2]
[(list(substrings(nums)))]
##### listing only the unique ones
set((list(substrings(nums))))
##### Applying a function cube to the substrings to make a powerset ####
[list(map(lambda n: pow(n,3),j)) for j in (set((list(substrings(nums)))))]
### list the substring, which is only a triplet
list(filter(lambda n: len(n)==3,[list(map(lambda n: pow(n,3),j)) for j in (set((list(substrings(nums)))))]))