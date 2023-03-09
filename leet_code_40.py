Con#cept, since the numbers are increasing in a continous way,so take the range of the last pointer plus so bascially a two
#pointer approach, the lower pointer greater than 0 and the end pointer greater than the last value and enumerate and take the
#enumerate i.
#https://leetcode.com/problems/kth-missing-positive-number/description/
#Kth Missing Positive Number
#Companies
#Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.
#Return the kth positive integer that is missing from this array.
#Example 1:
#Input: arr = [2,3,4,7,11], k = 5
#Output: 9
#Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
#Example 2:
#Input: arr = [1,2,3,4], k = 2
#Output: 6
#Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.
set([j for i in a for j,jd in enumerate(range(1,12),1) if j not in a])