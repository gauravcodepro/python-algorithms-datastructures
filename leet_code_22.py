#Longest Duplicate Substring https://leetcode.com/problems/longest-duplicate-substring/ (Hard)
#Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.
#Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".
#Example 1:
#Input: s = "banana"
#Output: "ana"
#Example 2:
#Input: s = "abcd"
#Output: ""
from collections import Counter
Counter([''.join(i) for i in [(s[i:i+3]) for i in range(len(s) - (3-1))]]).most_common(1)
Counter({'ban': 1, 'ana': 2, 'nan': 1})
[('ana', 2)]