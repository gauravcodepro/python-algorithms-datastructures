#https://leetcode.com/problems/sum-of-k-mirror-numbers/
#Sum of k-Mirror Numbers
#A k-mirror number is a positive integer without leading zeros that reads 
#the same both forward and backward in base-10 as well as in base-k.
#For example, 9 is a 2-mirror number. The representation of 9 in base-10 and 
#base-2 are 9 and 1001 respectively, which read the same both forward and backward.
#On the contrary, 4 is not a 2-mirror number. The representation of 4 in base-2 is 
#100, which does not read the same both forward and backward.
#Given the base k and the number n, return the sum of the n smallest k-mirror numbers.
#Input: k = 2, n = 5
#Output: 25
#Explanation:
#The 5 smallest 2-mirror numbers and their representations in base-2 are listed as follows:
#  base-10    base-2
#    1          1
#    3          11
#    5          101
#    7          111
#    9          1001
#Their sum = 1 + 3 + 5 + 7 + 9 = 25. 
#Input: k = 3, n = 7
#Output: 499
#Explanation:
#The 7 smallest 3-mirror numbers are and their representations in base-3 are listed as follows:
#  base-10    base-3
#    1          1
#    2          2
#    4          11
#    8          22
#    121        11111
#    151        12121
#    212        21212
#Their sum = 1 + 2 + 4 + 8 + 121 + 151 + 212 = 499.
#Input: k = 7, n = 17
#Output: 20379000
#Explanation: The 17 smallest 7-mirror numbers are:
#1, 2, 3, 4, 5, 6, 8, 121, 171, 242, 292, 16561, 65656, 2137312, 4602064, 6597956, 6958596

i used two nested maps and one filter nested comprehension to do this on the base 2 and the similar can
be done on any base.

list(filter(lambda n: [i for i in range(len(n)) if n[i][-1]=='Mirror'],(map(lambda n:[(n,'Mirror') if n[0]==n[-1] else (n,'No_Mirror') 
      for i in range(len(n))],(map(lambda n: list(n),map(lambda n: n[2:],map(bin,[i for i in range(1,10+1)]))))))))
      
[[(['1'], 'Mirror')],
 [(['1', '1'], 'Mirror'), (['1', '1'], 'Mirror')],
 [(['1', '0', '1'], 'Mirror'),
  (['1', '0', '1'], 'Mirror'),
  (['1', '0', '1'], 'Mirror')],
 [(['1', '1', '1'], 'Mirror'),
  (['1', '1', '1'], 'Mirror'),
  (['1', '1', '1'], 'Mirror')],
 [(['1', '0', '0', '1'], 'Mirror'),
  (['1', '0', '0', '1'], 'Mirror'),
  (['1', '0', '0', '1'], 'Mirror'),
  (['1', '0', '0', '1'], 'Mirror')]]