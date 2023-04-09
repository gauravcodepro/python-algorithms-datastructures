#https://leetcode.com/problems/find-smallest-letter-greater-than-target/
#Find Smallest Letter Greater Than Target
#You are given an array of characters letters that is sorted in non-decreasing order, 
#and a character target. There are at least two different characters in letters.
#Return the smallest character in letters that is lexicographically greater than target. 
#If such a character does not exist, return the first character in letters.
#Input: letters = ["c","f","j"], target = "a"
#Output: "c"
#Explanation: The smallest character that is lexicographically greater than 'a' in letters is 'c'.
#Input: letters = ["c","f","j"], target = "c"
#Output: "f"
#Explanation: The smallest character that is lexicographically greater than 'c' in letters is 'f'.
#Input: letters = ["x","x","y","y"], target = "z"
#Output: "x"
#Explanation: There are no characters in letters that is lexicographically greater than 'z' so we return letters[0].

chr(int(''.join(list(map(str,list(map(ord,sorted(letters)))[:1])))))