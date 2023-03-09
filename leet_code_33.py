#Letter Combinations of a Phone Number https://leetcode.com/problems/letter-combinations-of-a-phone-number/
#Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
#Return the answer in any order.
#A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#Example 1:
#Input: digits = "23"
#Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
#2=ABC
#3=def 
#Example 2:
#Input: digits = ""
#Output: []
#Example 3:
#Input: digits = "2"
#Output: ["a","b","c"]
from itertools import combinations
num=input('number':int) -> int
[(i,id) for i,id in enumerate([j for i in ([[(''.join(list(map(lambda n: chr(ord(n)+32),''.join([chr(c+65) 
                                                                                                 for c in range((15))])))))[i:i+3] 
        for i in range(0,len((''.join(list(map(lambda n: chr(ord(n)+32),''.join([chr(c+65) for c in range((15))])))))),3)]+
                            [''.join(list(map(lambda n: chr(ord(n)+32),[chr(c+65) for c in range(15,19)])))]+
                [''.join(list(map(lambda n: chr(ord(n)+32),[chr(c+65) for c in range(19,22)])))]+
                                [''.join(list(map(lambda n: (chr(ord(n)+32)),[chr(c+65) for c in range(22,26)])))]]) for j in i],2)]
print(list(combinations(id,num)))
[(2, 'abc'),
 (3, 'def'),
 (4, 'ghi'),
 (5, 'jkl'),
 (6, 'mno'),
 (7, 'pqrs'),
 (8, 'tuv'),
 (9, 'wxyz')]