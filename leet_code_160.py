#https://leetcode.com/problems/count-special-integers/
#Count Special Integers
#We call a positive integer special if all of its digits are distinct.
#Given a positive integer n, return the number of special integers that belong to the interval [1, n].
#Example 1:
#Input: n = 20
#Output: 19
#Explanation: All the integers from 1 to 20, except 11, are special. Thus, there are 19 special integers.
#Example 2:
#Input: n = 5
#Output: 5
#Explanation: All the integers from 1 to 5 are special.
#Example 3:
#Input: n = 135
#Output: 110
#Explanation: There are 110 integers from 1 to 135 that are special.
#Some of the integers that are not special are: 22, 114, and 131.

list(map(int,(map(lambda n: ''.join(n),list(filter(lambda n:len(n)==1,list(map(lambda n: list(n),
       map(lambda n: str(n),[i for i in range(21)])))))+list(filter(lambda n: len(set(n))!=1,
                   list(map(lambda n: list(n),map(lambda n: str(n),[i for i in range(21)])))))))))