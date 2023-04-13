#https://leetcode.com/problems/numbers-with-repeated-digits/
#Numbers With Repeated Digits
#Given an integer n, return the number of positive integers in the range [1, n] that have at least one repeated digit.
#Input: n = 20
#Output: 1
#Explanation: The only positive number (<= 20) with at least 1 repeated digit is 11.
#Input: n = 100
#Output: 10
#Explanation: The positive numbers (<= 100) with atleast 1 repeated digit are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.
#Input: n = 1000
#Output: 262

I made two nested comprehension to solve this. One to map the len and the second to map the expression.

list(map(lambda n:[(n[0],n[1],'True') if n[0]==n[1] else 'False' for i in n],
         (filter(lambda n: len(n)!=1,list(map(list,map(str,[i for i in range(input)])))))))

[['False', 'False'],
 [('1', '1', 'True'), ('1', '1', 'True')],
 ['False', 'False'],
 ['False', 'False'],
 ['False', 'False'],
 ['False', 'False'],
 ['False', 'False'],
 ['False', 'False'],
 ['False', 'False'],
 ['False', 'False'],
 ['False', 'False']]