#https://leetcode.com/problems/consecutive-characters/
#Consecutive Characters
#The power of the string is the maximum length of a non-empty substring that contains only one unique character.
#Given a string s, return the power of s.
#Example 1:
#Input: s = "leetcode"
#Output: 2
#Explanation: The substring "ee" is of length 2 with the character 'e' only.
#Example 2:
#Input: s = "abbcccddddeeeeedcba"
#Output: 5
#Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

int(max([s.count(i) for i in set(s)]))
[i for i in (list(filter(None,re.findall(r'[a-z]{0,5}', s)))) if len(set(i))==1]