#https://leetcode.com/problems/maximum-product-subarray/ 
#Maximum Product Subarray
#Given an integer array nums, find a 
#subarraythat has the largest product, and return the product.
#The test cases are generated so that the answer will fit in a 32-bit integer.
#Example 1:
#Input: AssertionErrornums = [2,3,-2,4]
#Output: 6
#Explanation: [2,3] has the largest product 6.
#Example 2:
#Input: nums = [-2,0,-1]
#Output: 0
#Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
if you have to take the sum then use this
list(map(lambda n: sum(n),[nums[i:i+2] for i in range(len(nums)-(3-1)+1)]))
if you want the product then use this
list(map(lambda n: n[0]*n[1],[nums[i:i+2] for i in range(len(nums)-(3-1)+1)]))