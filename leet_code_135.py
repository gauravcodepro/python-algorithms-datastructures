#https://leetcode.com/problems/count-unique-characters-of-all-substrings-of-a-given-string/
#Count Unique Characters of All Substrings of a Given String
#Let's define a function countUniqueChars(s) that returns the number of unique characters on s.
#For example, calling countUniqueChars(s) if s = "LEETCODE" then "L", "T", "C", "O", "D" 
#are the unique characters since they appear only once in s, therefore countUniqueChars(s) = 5.
#Given a string s, return the sum of countUniqueChars(t) where t is a substring of s. 
#The test cases are generated such that the answer fits in a 32-bit integer.
#Notice that some substrings can be repeated so in this case you have to count the repeated ones too.
#Input: s = "ABC"
#Output: 10
#Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
#Every substring is composed with only unique letters.
#Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
#Input: s = "ABA"
#Output: 8
#Explanation: The same as example 1, except countUniqueChars("ABA") = 1.
#Example 3:
#Input: s = "LEETCODE"
#Output: 92

list(map(lambda n: len(set(n)),list(filter(None,set([s[:i] 
      for i in range(len(s)+1)]+[s[i:i+2] for i in range(len(s)-(2-1))]+list(s))))))