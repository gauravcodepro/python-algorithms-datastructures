#https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
#Count Negative Numbers in a Sorted Matrix
#Given a m x n matrix grid which is sorted in non-increasing order 
#both row-wise and column-wise, return the number of negative numbers in grid.
#Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
#Output: 8
#Explanation: There are 8 negatives number in the matrix.
len([j for i in (list(map(lambda n:[i for i in n if i<1],grid))) for j in i])