#https://leetcode.com/problems/thousand-separator/
#Thousand Separator
#Given an integer n, add a dot (".") as the thousands separator and return it in string format.
#Example 1:
#Input: n = 987
#Output: "987"
#Example 2:
#Input: n = 1234
#Output: "1.234"
''.join([str(n) if len(str(n))==3 else str(n)[:1]+"."+str(n)[1:]])