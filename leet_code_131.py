#https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
#Longest Substring with At Least K Repeating Characters
#Given a string s and an integer k, return the length of the longest substring of s such that 
#the frequency of each character in this substring is greater than or equal to k.
#Input: s = "aaabb", k = 3
#Output: 3
#Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
#Input: s = "ababbc", k = 2
#Output: 5
#Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

list(map(lambda n:[(n,'True') if n.count(i)==3 and s not in n else 
        (n,'False') for i in set(n)],list(filter(None,[s[:i] for i in range(len(s)+1)]))))