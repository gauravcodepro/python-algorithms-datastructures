#https://leetcode.com/problems/four-divisors/
#Four Divisors
#Given an integer array nums, return the sum of divisors of the integers in that array that 
#have exactly four divisors. If there is no such integer in the array, return 0.
#Input: nums = [21,4,7]
#Output: 32
#Explanation: 
#21 has 4 divisors: 1, 3, 7, 21
#4 has 3 divisors: 1, 2, 4
#7 has 2 divisors: 1, 7
#The answer is the sum of divisors of 21 only.
#Example 2:
#Input: nums = [21,21]
#Output: 64
#Example 3:
#Input: nums = [1,2,3,4,5]
#Output: 0

sum([j for i in ((filter(lambda n: len(n)==4,map(lambda n: [n[i] for i in range(len(n)) 
           if 21%n[i]==0],(map(lambda n: [i for i in range(1,n+1)],nums)))))) for j in i])

sum([j for i in ((filter(lambda n: len(n)==4,map(lambda n: [n[i] for i in range(len(n)) 
          if 4%n[i]==0],(map(lambda n: [i for i in range(1,n+1)],nums)))))) for j in i])

sum([j for i in ((filter(lambda n: len(n)==4,map(lambda n: [n[i] for i in range(len(n)) 
          if 7%n[i]==0],(map(lambda n: [i for i in range(1,n+1)],nums)))))) for j in i])