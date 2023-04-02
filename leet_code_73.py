#https://leetcode.com/problems/count-number-of-nice-subarrays/
#Count Number of Nice Subarrays
#Given an array of integers nums and an integer k. 
#A continuous subarray is called nice if there are k odd numbers on it.
#Return the number of nice sub-arrays.
#Input: nums = [1,1,2,1,1], k = 3
#Output: 2
#Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
nums = [1,1,2,1,1]
list(filter(lambda n: [i for i in n if n.count(i%2==1)==3],list(filter(lambda n: len(n) >= 3,[nums[i:i+3] 
          for i in range(len(nums))]+[nums[i:i+4] 
                for i in range(len(nums))]+[nums[i:i+5] for i in range(len(nums))]))))