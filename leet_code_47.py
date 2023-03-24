#https://leetcode.com/problems/single-number-ii/
#Given an integer array nums where every element appears three times except 
#or one, which appears exactly once. Find the single element and return it.
#You must implement a solution with a linear runtime complexity and use only constant extra space.
Input: nums = [2,2,3,2]
Output: 3
[i for i in set(nums) if nums.count(i)==1]

#https://leetcode.com/problems/repeated-dna-sequences/
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.
For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.
Given a string s that represents a DNA sequence, return all the 10-letter-long sequences 
(substrings) that occur more than once in a DNA molecule. You may return the answer in any order.
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
[i for i in [s[i:i+9] for i in range(len(s)-(10-1))] 
               if [s[i:i+9] for i in range(len(s)-(10-1))].count(i) >= 2]