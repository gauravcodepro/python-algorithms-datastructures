#https://leetcode.com/problems/find-all-anagrams-in-a-string/
#Find All Anagrams in a String
#Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.Input: s = "cbaebabacd", p = "abc"
#Output: [0,6]
#Explanation:
#The substring with start index = 0 is "cba", which is an anagram of "abc".
#The substring with start index = 6 is "bac", which is an anagram of "abc".
#Input: s = "abab", p = "ab"
#Output: [0,1,2]
#Explanation:
#The substring with start index = 0 is "ab", which is an anagram of "ab".
#The substring with start index = 1 is "ba", which is an anagram of "ab".
#The substring with start index = 2 is "ab", which is an anagram of "ab".

list(map(lambda n:'True'if sorted(n)==sorted('abc') else 'False',[s[i:i+3] for i in range(len(s)-(3-1))]))

[j.start() for i in list(filter(lambda n:sorted(n)==sorted('abc'),[s[i:i+3] 
               for i in range(len(s)-(3-1))])) for j in re.finditer(i,s)]
