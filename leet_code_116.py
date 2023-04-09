#https://leetcode.com/problems/search-insert-position/
#Search Insert Position
#Given a sorted array of distinct integers and a target value, return the index if the target is found. 
#If not, return the index where it would be if it were inserted in order.
#You must write an algorithm with O(log n) runtime complexity.
#Example 1:
#Input: nums = [1,3,5,6], target = 5
#Output: 2
#Example 2:
#Input: nums = [1,3,5,6], target = 2
#Output: 1
#Example 3:
#Input: nums = [1,3,5,6], target = 7
#Output: 4
[i for i in range(len(nums)) if target==nums[i]],
    [i for i in range(len(sorted(nums))) if target < nums[i]][:1],
        len([i for i in range(len(sorted(nums))) if target > nums[-1]])
