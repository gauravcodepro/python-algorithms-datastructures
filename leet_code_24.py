#Palindrome Partitioning II (Hard) Leet code
#Given a string s, partition s such that every substring of the partition is a palindrome
#Return the minimum cuts needed for a palindrome partitioning of s.
#Example 1:
#Input: s = "aab"
#Output: 1
#Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
#Example 2:
#Input: s = "a"
#Output: 0
#Example 3:
#Input: s = "ab"
#Output: 1
from more_itertools import chunked
[print('True') for i in ([''.join(i) for i in list(chunked(s,2))]) if sorted(i)==sorted(i[::-1])]
['aa', 'b']
# for generating a range of lists by iterating over the string and providing the length of the string as an iterator
[list(map(lambda n: ''.join(n),i)) for i in (list(chunked(s,i)) for i,id in enumerate(s,1))]
[['a', 'a', 'b'], ['aa', 'b'], ['aab']]