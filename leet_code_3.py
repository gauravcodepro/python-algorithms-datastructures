# Longest Valid Parentheses (category hard)
#Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
#substring
#Example 1:
#Input: s = "(()"
#Output: 2
#Explanation: The longest valid parentheses substring is "()".
#Example 2:
#Input: s = ")()())"
#Output: 4
#Explanation: The longest valid parentheses substring is "()()".
#Example 3:
#Input: s = ""
#Output: 0
s = ")()())"
set([s.count('()') for i in s])
{2}
and multiply the number by 2 as the parenthese contains 2.