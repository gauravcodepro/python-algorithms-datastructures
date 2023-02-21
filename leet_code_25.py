#Shortest Subarray with Sum at Least K (Hard) Leet code 
#Given an integer array nums and an integer k, return the length of the shortest non-empty 
#subarray of nums with a sum of at least k. If there is no such subarray, return -1.
#A subarray is a contiguous part of an array.
#Example 1:
#Input: nums = [1], k = 1
#Output: 1
#Example 2:
#Input: nums = [1,2], k = 4
#Output: -1
#Example 3:
#Input: nums = [2,-1,2], k = 3
#Output: 3
#print a bool
a = [2,-1,2], k = 3 
[print('True') for i in ((a[i:i+3]) for i in range(len(a) - (3-1))) if sum(i)==k]
True
# print the subarray
a = [2,-1,2], k = 3
[print(i) for i in ((a[i:i+3]) for i in range(len(a) - (3-1))) if sum(i)==k]
[2, -1, 2]