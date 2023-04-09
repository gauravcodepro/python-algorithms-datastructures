#https://leetcode.com/problems/is-subsequence/
#Is Subsequence
#Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#A subsequence of a string is a new string that is formed from the original string by deleting 
#some (can be none) of the characters without disturbing the relative positions of the remaining 
#characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
#Input: s = "abc", t = "ahbgdc"
#Output: true4
#Input: s = "axc", t = "ahbgdc"
#Output: false

'True' if ''.join(re.findall(r'[a-c]{,3}',t))=="abc" else "False"