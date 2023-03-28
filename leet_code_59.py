#https://leetcode.com/problems/set-mismatch/
#Set Mismatch
#You have a set of integers s, which originally contains all the numbers from 1 to n. 
#Unfortunately, due to some error, one of the numbers in s got duplicated to another number 
#in the set, which results in repetition of one number and loss of another number.
#You are given an integer array nums representing the data status of this set after the error.
#Find the number that occurs twice and the number that is missing and return them in the form of an array.
#Input: nums = [1,2,2,4]
#Output: [2,3]
#Input: nums = [1,1]
#Output: [1,2]
nums = [1,2,2,4]
[(nums[i],[i for i in range(1,5)][i],'True') if nums[i]==[i for i in range(1,5)][i] 
             else (nums[i],[i for i in range(1,5)][i],'False') for i in range(len(nums))]
             [(1, 1, 'True'), (2, 2, 'True'), (2, 3, 'False'), (4, 4, 'True')]