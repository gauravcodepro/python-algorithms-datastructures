#https://leetcode.com/problems/count-numbers-with-unique-digits/
#Count Numbers with Unique Digits
#Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.
#Input: n = 2
#Output: 91
#Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99
len(list(filter(lambda n: len(n)==1,list(map(tuple,[j for i in ([list(map(list,(list(map(str,[i for i in range(0,101)])))))])
                for j in i])))) + list(filter(lambda n: n[0]!=n[1],list(filter(lambda n: len(n)==2,
                                    list(map(tuple,[j for i in ([list(map(list,(list(map(str,[i for i in range(0,101)])))))]) for j in i])))))))
Concept, what i did is created the range and then mapped the tuples and then apply the filter two times, first filtering the ones with the len=! and
second filtering the ones with the len == 2 and the tuple n[0]!=n[1] and then calculating the total jointed length. Simple solution