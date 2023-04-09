#https://leetcode.com/problems/concatenated-words/
#Concatenated Words
#Given an array of strings words (without duplicates), return all the concatenated words in the given list of words.
#A concatenated word is defined as a string that is comprised entirely of at least two shorter words (not necesssarily distinct) in the given array.
#Input: words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
#Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
#Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
#"dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
#"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
#Input: words = ["cat","dog","catdog"]
#Output: ["catdog"]

set(list(filter(lambda n: n not in list(filter(lambda n: len(n) <= 4,
      sorted(words,key=lambda n: len(n)))),(filter(lambda n: n!='False',[words[i] 
          if all([j in words[i]]) else 'False' for i in range(len(words)) for 
             j in list(filter(lambda n: len(n) <= 4,sorted(words,key=lambda n: len(n))))])))))