#Minimum Window Substring (Hard)
#Given two strings s and t of lengths m and n respectively, return the minimum window substring
#of s such that every character in t (including duplicates) is included in the window. 
#If there is no such substring, return the empty string "".
#The testcases will be generated such that the answer is unique.
#Example 1:
#Input: s = "ADOBECODEBANC", t = "ABC"
#Output: "BANC"
#Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
#Example 2:
#Input: s = "a", t = "a"
#Output: "a"
#Explanation: The entire string s is the minimum window.
#Example 3:
#Input: s = "a", t = "aa"
#Output: ""
#Explanation: Both 'a's from t must be included in the window.
#Since the largest window of s only has one 'a', return empty string.
from more_itertools import windowed
s = "ADOBECODEBANC"
[print (i,(i.count('A'),i.count('B'), i.count('C'))) for i in [''.join(i) for i in (list(windowed(s,4)))]]
ADOB (1, 1, 0)
DOBE (0, 1, 0)
OBEC (0, 1, 1)
BECO (0, 1, 1)
ECOD (0, 0, 1)
CODE (0, 0, 1)
ODEB (0, 1, 0)
DEBA (1, 1, 0)
EBAN (1, 1, 0)
BANC (1, 1, 1)