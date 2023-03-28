#https://leetcode.com/problems/wiggle-subsequence/
#Wiggle Subsequence
#A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. 
#The first difference (if one exists) may be either positive or negative. A sequence with one element and a sequence 
#with two non-equal elements are trivially wiggle sequences.
#For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) alternate between positive and negative.
#In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences. The first is not because
#its first two differences are positive, and the second is not because its last difference is zero.
#A subsequence is obtained by deleting some elements (possibly zero) from the 
#original sequence, leaving the remaining elements in their original order.
#Given an integer array nums, return the length of the longest wiggle subsequence of nums.
['True' if [(nums[i+1]-nums[i])for i in range(len(nums)-1)][i] > 0 and [(nums[i+1]-nums[i])for i in range(len(nums)-1)][i+1] < 0 else 'False' for i 
                  in range(len([(nums[i+1]-nums[i])for i in range(len(nums)-1)])-1)]
                  ['True', 'False', 'True', 'False']
concept what i did was a simple comprehension to subtract the alternate numbers and then a simple comprehension to
say that the number is greater than 0 or number is less than 0. 