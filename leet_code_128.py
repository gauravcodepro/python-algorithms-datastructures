#https://leetcode.com/problems/sum-of-square-numbers/
#Sum of Square Numbers
#Input: c = 5
#Output: true
#Explanation: 1 * 1 + 2 * 2 = 5
#Input: c = 3
#Output: false
#Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

[(c-i) for i in [i*i for i in range(c+1)] if (c-i) in [i*i for i in range(c+1)]]