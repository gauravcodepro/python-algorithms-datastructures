#https://leetcode.com/problems/check-if-all-the-integers-in-a-range-are-covered/
#Check if All the Integers in a Range Are Covered
#You are given a 2D integer array ranges and two integers left and right. 
#Each ranges[i] = [starti, endi] represents an inclusive interval between starti and endi.
#Return true if each integer in the inclusive range [left, right] is covered by 
#at least one interval in ranges. Return false otherwise.
#An integer x is covered by an interval ranges[i] = [starti, endi] if starti <= x <= endi.
#Input: ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
#Output: true
#Explanation: Every integer between 2 and 5 is covered:
#- 2 is covered by the first range.
#- 3 and 4 are covered by the second range.
#- 5 is covered by the third range.
#Input: ranges = [[1,10],[10,20]], left = 21, right = 21
#Output: false
#Explanation: 21 is not covered by any range.

'True' if all([i for i in range(2,5+1)]) in [j for i in ranges for j in i] else 'False'