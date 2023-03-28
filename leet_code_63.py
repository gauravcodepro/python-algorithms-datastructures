#https://leetcode.com/problems/minimum-common-value/
#Minimum Common Value
#Given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
#return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.
#Input: nums1 = [1,2,3], nums2 = [2,4]
#Output: 2
#Explanation: The smallest element common to both arrays is 2, so we return 2.
#set cardinality way
set(nums1).intersection(set(nums2))
#comprehension way
[i for i in nums1 if i in nums2]