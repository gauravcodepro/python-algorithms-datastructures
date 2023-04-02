#https://leetcode.com/problems/subarrays-with-k-different-integers/
#Subarrays with K Different Integers
#Given an integer array nums and an integer k, return the number of good subarrays of nums.
#A good array is an array where the number of different integers in that array is exactly k.
#For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
#A subarray is a contiguous part of an array.
#Input: nums = [1,2,1,2,3], k = 2
#Output: 7
#Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
[list(map(lambda n: (n,'True') if len(set(n))==2 else (n,'False'),list(map(lambda n: tuple(n),
    list(filter(lambda n: len(n)>=2,[nums[i:i+2] for i in range(len(nums))]+[nums[i:i+3] 
      for i in range(len(nums))]+[nums[i:i+4] for i in range(len(nums))]+[nums[i:i+5] for 
        i in range(len(nums))]+[nums[i::2] for i in range(len(nums))]+[nums[i::3] for i 
          in range(len(nums))]+[nums[i::4] for i in range(len(nums))]+[nums[i::4] for i in range(len(nums))]))))))]