#https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
#Find All Numbers Disappeared in an Array
#Given an array nums of n integers where nums[i] is in the range [1, n], 
#return an array of all the integers in the range [1, n] that do not appear in nums.
#Input: nums = [4,3,2,7,8,2,3,1]
#Output: [5,6]
#Input: nums = [1,1]
#Output: [2]

set([i for i in range(min(sorted(nums)),max(sorted(nums))+1)])^set(nums)