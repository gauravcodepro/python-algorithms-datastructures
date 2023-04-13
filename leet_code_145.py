#https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/
#Check If All 1's Are at Least Length K Places Away
#Given an binary array nums and an integer k, return true if all 1's are at least k places away from each other, otherwise return false.
#Input: nums = [1,0,0,0,1,0,0,1], k = 2
#Output: true
#Explanation: Each of the 1s are at least 2 places away from each other.
#Input: nums = [1,0,0,1,0,1], k = 2
#Output: false
#Explanation: The second 1 and third 1 are only one apart from each other.

['True' if abs([i for i in range(len(nums)) if nums[i]==1][i]-[i for i in range(len(nums)) if nums[i]==1][i+1]) > 2 
           else 'False' for i in range(len([i for i in range(len(nums)) if nums[i]==1])-1)]