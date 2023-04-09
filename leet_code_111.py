#https://leetcode.com/problems/max-consecutive-ones/
#Max Consecutive Ones
#Given a binary array nums, return the maximum number of consecutive 1's in the array.
#Input: nums = [1,1,0,1,1,1]
#Output: 3
#Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
#Input: nums = [1,0,1,1,0,1]
#Output: 2
sorted(re.findall(r'[1]{,6}',''.join(list(map(str,nums)))),reverse=True)[:1]