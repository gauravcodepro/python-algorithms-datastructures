#https://leetcode.com/problems/palindromic-substrings/
#Palindromic Substrings
#Given a string s, return the number of palindromic substrings in it.
#A string is a palindrome when it reads the same backward as forward.
#A substring is a contiguous sequence of characters within the string.
#Input: s = "abc"
#Output: 3
#Explanation: Three palindromic strings: "a", "b", "c".
#Input: s = "aaa"
#Output: 6
#Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
[(i,'True') if i==i[::-1] else (i,'False') for i 
         in (list(filter(None,[s[:i] for i in range(len(s)+1)]))+list(s))]
[('a', 'True'),
 ('ab', 'False'),
 ('abc', 'False'),
 ('a', 'True'),
 ('b', 'True'),
 ('c', 'True')]