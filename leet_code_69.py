#https://leetcode.com/problems/monotonic-array/
#Monotonic Array
#An array is monotonic if it is either monotone increasing or monotone decreasing.
#An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. 
#An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
#Given an integer array nums, return true if the given array is monotonic, or false otherwise.
#Example 1:
#Input: nums = [1,2,2,3]
#Output: true
#Example 2:
#Input: nums = [6,5,4,4]
#Output: true
#Example 3:
#Input: nums = [1,3,2]
#Output: false
#i implemented the binary sort range(len) to solve this
nums = [1,2,2,3]
['True' if (nums[j] <= nums[j+1] or nums[j] >= nums[j+1] ) else 'False' for i in range(len(nums)-1) for j in range(len(nums)-i-1)]