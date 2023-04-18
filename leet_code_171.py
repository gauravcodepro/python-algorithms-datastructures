#https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
#Find All Numbers Disappeared in an Array
#Given an array nums of n integers where nums[i] is in the range [1, n], 
#return an array of all the integers in the range [1, n] that do not appear in nums.
#Input: nums = [4,3,2,7,8,2,3,1]
#Output: [5,6]
[i for i in (set([i for i,id in enumerate(nums,1)])) if i not in nums]