#https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/
#Check if All Characters Have Equal Number of Occurrences
#Given a string s, return true if s is a good string, or false otherwise.
#A string s is good if all the characters that appear in s have the same number of occurrences (i.e., the same frequency).
#Input: s = "abacbc"
#Output: true
#Explanation: The characters that appear in s are 'a', 'b', and 'c'. All characters occur 2 times in s.
#Input: s = "aaabb"
#Output: false
#Explanation: The characters that appear in s are 'a' and 'b'.
#'a' occurs 3 times while 'b' occurs 2 times, which is not the same number of times.

'True' if len(set([s.count(i) for i in set(s)]))==1 else 'False'