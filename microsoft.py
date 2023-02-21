# microsoft top interview question
#Find all palindrome substrings
#Problem Statement: Given a string, find all non-single letter substrings that are palindromes.
a="poppopo"
from more_itertools import windowed
from stringtools.analysers import *
[''.join(i) for i in (list(windowed(a,3)))], [(is_palindrome(j)) for j in (''.join(i) for i in list(windowed(a,3)))]

# Microsoft top problem statement: Given a positive integer, target, print all possible combinations of numbers in alternate orders that add up to the number keeping the tuple range to the 2.
a=10
[list(zip([i for i in range(a-1, 0, -1)],[i for i in range(1, a, 1)]))]
[[(9, 1), (8, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (2, 8), (1, 9)]]