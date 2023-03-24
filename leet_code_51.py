https://leetcode.com/problems/search-a-2d-matrix/
You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.
# two ways to solve this 
# first converting it into a single linear array
# and then searching in it
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
[j for i in matrix for j in i].__contains__(3)
# using a map and a expression approach using the
#generator
[list(map(lambda n: 'True' if n.__contains__(3) else 'False',matrix))]