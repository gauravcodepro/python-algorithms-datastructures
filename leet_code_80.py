#https://leetcode.com/problems/first-unique-character-in-a-string/
#Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.
#First Unique Character in a String
#Example 1:
#Input: s = "leetcode"
#Output: 0
#Example 2:
#Input: s = "loveleetcode"
#Output: 2
sorted([(i,s.find(i)) for i in (sorted([i for i in 
             set(s) if s.count(i)==1]))],key=lambda n: n[1])[:1]
             [('l', 0)]

#https://leetcode.com/problems/top-k-frequent-words/
#Top K Frequent Words
#Given an array of strings words and an integer k, return the k most frequent strings.
#Return the answer sorted by the frequency from highest to lowest. 
#Sort the words with the same frequency by their lexicographical order.
#Input: words = ["i","love","leetcode","i","love","coding"], k = 2
#Output: ["i","love"]
#Explanation: "i" and "love" are the two most frequent words.
#Note that "i" comes before "love" due to a lower alphabetical order.
sorted([i for i in set(words) if words.count(i) == 2])