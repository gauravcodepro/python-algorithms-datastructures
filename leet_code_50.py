#https://leetcode.com/problems/word-break/
#Given a string s and a dictionary of strings wordDict, return true if s can be segmented
#into a space-separated sequence of one or more dictionary words.
#Note that the same word in the dictionary may be reused multiple times in the segmentation.
#Input: s = "leetcode", wordDict = ["leet","code"]
#Output: true
#Explanation: Return true because "leetcode" can be segmented as "leet code".
#Input: s = "applepenapple", wordDict = ["apple","pen"]
#Output: true
#Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#Note that you are allowed to reuse a dictionary word.
#Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
#Output: false
s = "leetcode"
wordDict = ["leet","code"]
# concept first calculate the length of the words in the wordDict
[list(map(lambda n: len(n),wordDict))]
# now make the iterative word break according to the length 
[s[i:i+4] for i in range(len(s) -(4-1))]
# write a generator and ternary expression
['True' if i in [s[i:i+4] for i in range(len(s) -(4-1))] else 'False' for i in wordDict]