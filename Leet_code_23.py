#First Missing Positive (Hard) Leet code
#Given an unsorted integer array nums, return the smallest missing positive integer.
#You must implement an algorithm that runs in O(n) time and uses constant extra space.
#Example 1:
#Input: nums = [1,2,0]
#Output: 3
#Explanation: The numbers in the range [1,2] are all in the array.
#Example 2:
#Input: nums = [3,4,-1,1]
#Output: 2
#Explanation: 1 is in the array but 2 is missing.
#Example 3:
#Input: nums = [7,8,9,11,12]
#Output: 1
#Explanation: The smallest positive integer 1 is missing.
See the approach, i am enumerating the list at the start of the list and then finding the id in the original list. 
# using the index based solution
[(i) for i,id in (enumerate(sorted(nums),7)) if i not in nums]
a = sorted([1,2,0])
[(i) for i,id in (enumerate(sorted(a),1)) if i not in a]
[3]
a = sorted([7,8,9,11,12])
[(i) for i,id in (enumerate(sorted(a),7)) if i not in a]
[10]