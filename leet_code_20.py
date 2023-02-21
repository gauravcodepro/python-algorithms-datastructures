#leet code
#K-Similar Strings (Hard)
#Strings s1 and s2 are k-similar (for some non-negative integer k) if we can swap the positions of 
# two letters in s1 exactly k times so that the resulting string equals s2.
#Given two anagrams s1 and s2, return the smallest k for which s1 and s2 are k-similar.
#Example 1:
#Input: s1 = "ab", s2 = "ba"
#Output: 1
#Explanation: The two string are 1-similar because we can use one swap to change s1 to s2: "ab" --> "ba".
#Example 2:
#Input: s1 = "abc", s2 = "bca"
#Output: 2
#Explanation: The two strings are 2-similar because we can use two swaps to change s1 to s2: "abc" --> "bac" --> "bca".
a='abc'
from more_itertools import circular_shifts
len([i for i in ([''.join(i) for i in (circular_shifts(a))]) if sorted(i)==sorted('abc')])-1