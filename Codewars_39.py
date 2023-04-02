#https://leetcode.com/problems/shifting-letters/
#Shifting Letters
#You are given a string s of lowercase English letters and an integer array shifts of the same length.
#Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').
#For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
#Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.
#Return the final string after all such shifts to s are applied.
#Example 1:
#Input: s = "abc", shifts = [3,5,9]
#Output: "rpl"
#Explanation: We start with "abc".
#After shifting the first 1 letters of s by 3, we have "dbc".
#After shifting the first 2 letters of s by 5, we have "igc".
#After shifting the first 3 letters of s by 9, we have "rpl", the answer.
#Input: s = "abc", shifts = [3,5,9]
#Output: "rpl"
#Explanation: We start with "abc".
#After shifting the first 1 letters of s by 3, we have "dbc".
#After shifting the first 2 letters of s by 5, we have "igc".
#After shifting the first 3 letters of s by 9, we have "rpl", the answer.
''.join([chr(ord(([s[i] for i in range(len(s))][0]))+sum(shifts)),
          chr(ord([s[i] for i in range(len(s))][1])+sum([shifts[1],shifts[2]])),
                     chr(ord([s[i] for i in range(len(s))][2])+shifts[2])])